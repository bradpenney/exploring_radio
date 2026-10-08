#!/usr/bin/env python3
"""Build the ISED Basic Qualification Anki deck for radio.bradpenney.io.

Source of truth: ISED's delimited question bank (anki/source/amat_basic_quest_delim.txt,
from https://apc-cap.ic.gc.ca/datafiles/amat_basic_quest.zip, modified 2025-07-15).
It lists each question's correct answer and three incorrect ones, but no A-D order.

Display order: where the printed PDF bank (parsed by parse_bank.py into
basic_questions.json) has exactly the same four options, its A-D order is kept, so
the cards match the printed bank. The two ISED files disagree on 11 questions (see
anki/README.md); those use the delimited file's text in a fixed shuffled order.

Card GUIDs are derived from the question ID, so re-importing a rebuilt deck updates
existing cards in place and keeps the learner's review history.

Usage:
    poetry install --with anki
    poetry run python anki/build_deck.py
"""

import csv
import html
import json
import random
import re
from pathlib import Path

import genanki

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "source" / "amat_basic_quest_delim.txt"
PDF_JSON = HERE / "basic_questions.json"
BANK_DATE = "2025-07-15"
OUT = HERE.parent / "docs" / "downloads" / f"ised_basic_qualification_{BANK_DATE}.apkg"

# Section titles from RIC-3 Issue 5 (March 2022), section 5.1.
SECTIONS = {
    "B-001": "Regulations and Policies",
    "B-002": "Operating and Procedures",
    "B-003": "Station Assembly, Practice and Safety",
    "B-004": "Circuit Components",
    "B-005": "Basic Electronics and Theory",
    "B-006": "Feedlines and Antenna Systems",
    "B-007": "Radio Wave Propagation",
    "B-008": "Interference and Suppression",
}

ROOT_DECK = f"ISED Basic Qualification ({BANK_DATE})"
# Fixed IDs: never change them, or re-imports create duplicate decks/note types.
MODEL_ID = 1735190207
DECK_ID_BASE = 1735190300

ATTRIBUTION = (
    "Questions reproduced from <i>Basic Qualification Question Bank for Amateur Radio "
    "Operator Certificate Examinations</i> (15 July 2025), Innovation, Science and "
    "Economic Development Canada. This is a copy of the version available at "
    "https://ised-isde.canada.ca/site/amateur-radio-operator-certificate-services/en/downloads "
    "and is not an official version. Deck by Exploring Radio (radio.bradpenney.io), "
    "free for non-commercial use."
)

CSS = """
.card { font-family: "IBM Plex Sans", -apple-system, "Segoe UI", sans-serif; font-size: 19px;
        line-height: 1.45; text-align: left; color: #1a202c; background: #fdfcf8; max-width: 720px;
        margin: 0 auto; padding: 4px 8px; }
.nightMode.card, .night_mode .card { color: #e6e6e6; background: #1a1a1a; }
.chip { display: inline-block; font-size: 13px; padding: 2px 8px; border-radius: 10px;
        background: #f59e0b; color: #1a1a1a; font-weight: 600; margin-bottom: 10px; }
.qid { font-size: 13px; color: #718096; margin-left: 6px; }
.question { font-weight: 600; margin: 6px 0 14px; }
.opts { list-style: none; padding: 0; margin: 0; }
.opts li { padding: 6px 10px; margin: 6px 0; border: 1px solid #cbd5e0; border-radius: 6px; }
.nightMode .opts li, .night_mode .opts li { border-color: #4a5568; }
.opts b { display: inline-block; width: 1.4em; }
.answer { margin-top: 14px; padding: 10px 12px; border-left: 4px solid #2f855a;
          background: rgba(47, 133, 90, 0.12); border-radius: 4px; }
.source { margin-top: 18px; font-size: 12px; color: #718096; }
"""

FRONT = """<span class="chip">{{Section}}</span><span class="qid">{{ID}}</span>
<div class="question">{{Question}}</div>
<ul class="opts">
<li><b>A</b>{{A}}</li><li><b>B</b>{{B}}</li><li><b>C</b>{{C}}</li><li><b>D</b>{{D}}</li>
</ul>"""

BACK = """{{FrontSide}}
<div class="answer"><b>{{Answer}}</b> &nbsp;{{AnswerText}}</div>
<div class="source">ISED Basic question bank, """ + BANK_DATE + """ · {{ID}}</div>"""

MODEL = genanki.Model(
    MODEL_ID,
    "Exploring Radio: ISED Basic (multiple choice)",
    fields=[{"name": n} for n in
            ("ID", "Section", "Question", "A", "B", "C", "D", "Answer", "AnswerText")],
    templates=[{"name": "Question → Answer", "qfmt": FRONT, "afmt": BACK}],
    css=CSS,
    sort_field_index=0,
)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def load_txt():
    with open(SOURCE, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter=";"))[1:]
    out = {}
    for r in rows:
        qid = r[0].strip()
        out[qid] = {"question": norm(r[1]), "correct": norm(r[2]),
                    "incorrect": [norm(x) for x in r[3:6]]}
    return out


def ordered_options(qid, txt, pdf):
    """Return (options dict A-D, correct letter)."""
    p = pdf.get(qid)
    four = [txt["correct"]] + txt["incorrect"]
    if p and sorted(map(norm, p["options"].values())) == sorted(four) \
            and norm(p["question"]) == txt["question"]:
        opts = {k: norm(v) for k, v in p["options"].items()}
        letter = next(k for k, v in opts.items() if v == txt["correct"])
        return opts, letter, True
    rnd = random.Random(qid)
    rnd.shuffle(four)
    opts = dict(zip("ABCD", four))
    letter = next(k for k, v in opts.items() if v == txt["correct"])
    return opts, letter, False


def main():
    txt = load_txt()
    pdf = {q["id"]: q for q in json.loads(PDF_JSON.read_text(encoding="utf-8"))}
    assert len(txt) == 984, len(txt)
    decks = {}
    for i, (code, title) in enumerate(SECTIONS.items()):
        d = genanki.Deck(DECK_ID_BASE + i, f"{ROOT_DECK}::{code} {title}")
        d.description = ATTRIBUTION
        decks[code] = d
    disputed = []
    for qid in sorted(txt):
        t = txt[qid]
        opts, letter, from_pdf = ordered_options(qid, t, pdf)
        if not from_pdf:
            disputed.append(qid)
        section = qid[:5]
        e = html.escape
        note = genanki.Note(
            model=MODEL,
            fields=[qid, f"{section} {SECTIONS[section]}", e(t["question"]),
                    e(opts["A"]), e(opts["B"]), e(opts["C"]), e(opts["D"]),
                    letter, e(t["correct"])],
            guid=genanki.guid_for("exploring-radio-ised-basic", qid),
            tags=[f"ISED_Basic::{section}", f"ISED_Basic::{qid[:9]}"],
        )
        decks[section].add_note(note)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    genanki.Package(list(decks.values())).write_to_file(str(OUT))
    print(f"wrote {OUT.relative_to(HERE.parent)}: {len(txt)} notes, "
          f"{len(disputed)} using delimited-file order: {', '.join(disputed)}")


if __name__ == "__main__":
    main()
