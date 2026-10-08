# Exploring Radio

Source for [radio.bradpenney.io](https://radio.bradpenney.io): amateur radio from
first principles, from studying for the Canadian Amateur Radio Operator Certificate
(Basic Qualification) to antennas, propagation, and getting on the air.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and Poetry.

```bash
poetry install
poetry run mkdocs serve -a 127.0.0.1:8471
poetry run mkdocs build --strict
```

Schematics are generated from Python (schemdraw); see `schematics/README.md`.
Editorial standards live in `CLAUDE.md`.
