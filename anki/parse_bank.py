#!/usr/bin/env python3
"""Parse ISED's Basic Qualification question bank PDF into JSON.

The PDF is two columns per page. Each column is extracted separately with
`pdftotext -layout` (poppler), cropped at x=240pt, then read in order: page 1
left, page 1 right, page 2 left, ... A question looks like:

    B-001-001-001     (A)
    Question text, possibly
    over several lines?
    A   option text
        continued
    B   ...

Usage:
    python3 anki/parse_bank.py <bank.pdf> anki/basic_questions.json
"""

import json
import re
import subprocess
import sys

ID_RE = re.compile(r"^\s*(B-00[1-8]-\d{3}-\d{3})\s*\(([A-D])\)\s*$")
OPT_RE = re.compile(r"^([A-D])(?:\s{2,}(.*)|\s*)$")
SPLIT_X = 240


def page_count(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))


def column(pdf, page, left):
    x, w = (0, SPLIT_X) if left else (SPLIT_X, 612 - SPLIT_X)
    args = ["pdftotext", "-layout", "-f", str(page), "-l", str(page),
            "-x", str(x), "-y", "0", "-W", str(w), "-H", "792", pdf, "-"]
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def join(lines):
    out = ""
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        if out.endswith("-") and not out.endswith(" -"):
            out += ln
        else:
            out += (" " if out else "") + ln
    return out


def parse(pdf):
    lines = []
    for p in range(1, page_count(pdf) + 1):
        for left in (True, False):
            lines += column(pdf, p, left).splitlines()
    questions, cur, part = [], None, None
    for raw in lines:
        m = ID_RE.match(raw)
        if m:
            if cur:
                questions.append(cur)
            cur = {"id": m.group(1), "answer": m.group(2), "q": [], "opts": {}}
            part = "q"
            continue
        if cur is None:
            continue
        o = OPT_RE.match(raw)
        if o and (part == "q" or part in "ABCD") and o.group(1) not in cur["opts"]:
            # an option letter must come in order A, B, C, D
            expected = "ABCD"[len(cur["opts"])]
            if o.group(1) == expected:
                part = o.group(1)
                cur["opts"][part] = [o.group(2) or ""]
                continue
        if part == "q":
            cur["q"].append(raw)
        elif part in "ABCD":
            if part == "D" and not raw.strip() and cur["opts"]["D"] != [""]:
                part = "done"  # blank line after D ends the question
                continue
            cur["opts"][part].append(raw)
    if cur:
        questions.append(cur)
    result = []
    for q in questions:
        item = {
            "id": q["id"],
            "section": q["id"][:5],
            "topic": q["id"][:9],
            "question": join(q["q"]),
            "options": {k: join(v) for k, v in q["opts"].items()},
            "answer": q["answer"],
        }
        result.append(item)
    return result


def validate(qs):
    problems = []
    ids = [q["id"] for q in qs]
    if len(ids) != len(set(ids)):
        problems.append("duplicate ids")
    for q in qs:
        if sorted(q["options"]) != ["A", "B", "C", "D"]:
            problems.append(f"{q['id']}: options {sorted(q['options'])}")
        if not q["question"]:
            problems.append(f"{q['id']}: empty question")
        for k, v in q["options"].items():
            if not v:
                problems.append(f"{q['id']}: empty option {k}")
    return problems


if __name__ == "__main__":
    qs = parse(sys.argv[1])
    probs = validate(qs)
    for p in probs:
        print("PROBLEM", p, file=sys.stderr)
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=1)
    print(f"{len(qs)} questions, {len(probs)} problems")
    sys.exit(1 if probs else 0)
