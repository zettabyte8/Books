# BUILD INSTRUCTIONS — v2.1

Supersedes the v2.0 set. Delete the old files before building; names and numbers have changed.

## Assemble
Requires Python 3 and Pandoc.

```bash
mkdir book && cd book
# save all 21 files here
python3 01_build.py            # concatenates into manuscript_full.md
python3 01_build.py --all      # also emits .docx, .epub, .pdf
```

For PDF, install `texlive-xetex` or use `--pdf-engine=weasyprint`. Name the cover `cover.jpg` and the plates `plate_1.jpg`, `plate_2.jpg`, `plate_3.jpg` in the same directory.

## Order
00 readme · 01 build · 02 front matter · 03–14 chapters 1–13 · 15–19 appendices A–E · 20 proposal

## v2.1 changes
- **New Chapter 9**, "Elsewhere," on state media outside the Atlantic. Part III renumbered 10–13. Every cross-reference updated.
- **Chapter 3** gains a section on the Overton window; the term is now used rather than merely glossed.
- **Chapter 6** names a specialist (Welch) and adds a source-problem box on Speer's memoir. The searchlight figure is corrected from "8 km intervals" to beams reaching 8 km altitude.

## Before submission
- Specialist review, Chapters 6 and 9.
- Verify every entry in Appendix D against the physical text.
- Commission an index.
- Permissions for all primary-source excerpts.