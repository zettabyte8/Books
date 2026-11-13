# BUILD INSTRUCTIONS

This manuscript is plain Markdown, one file per section, numbered for assembly order.

## Why there are no hosted download links
Chat clients can't host files. These are code blocks — copy each into a text editor and save under the filename in its header. That gives you the full source set. The script below then produces every distributable format locally.

## Assemble and build
Requires Python 3 and Pandoc.

```bash
mkdir book && cd book
# save every .md file here, then:
python3 build.py            # concatenates into manuscript_full.md
python3 build.py --all      # also emits .docx, .epub, .pdf
```

`build.py --all` calls Pandoc three times. For PDF, Pandoc needs a LaTeX engine (`apt install texlive-xetex`) or use `--pdf-engine=weasyprint`.

## File order
00 front matter, 01–12 chapters, 13 glossary, 14 sources, 15 prompt history, 16 activities.

## Before you send it to a publisher
- Replace the placeholder imprint line in 00.
- Have a human proofread the Contested boxes for tone.
- Verify every item in 14 against the physical text — do not trust a generated citation list.
- Add an index; Pandoc will not make one.