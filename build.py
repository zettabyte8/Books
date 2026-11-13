#!/usr/bin/env python3
"""Assemble and build the manuscript. Usage: python3 build.py [--all]"""
import glob, subprocess, sys, os

ORDER = sorted(glob.glob("*.md"))
ORDER = [f for f in ORDER if f != "manuscript_full.md"]
OUT = "manuscript_full.md"

def main():
    with open(OUT, "w", encoding="utf-8") as out:
        for f in ORDER:
            out.write(open(f, encoding="utf-8").read().rstrip() + "\n\n\\newpage\n\n")
    print(f"wrote {OUT} from {len(ORDER)} files")
    if "--all" in sys.argv:
        meta = ["-M", "title=The Architecture of Consent and Control",
                "-M", "author=Thomas G. Coleman, with Gemini and Venice AI",
                "-M", "lang=en", "--toc", "--toc-depth=2",
                "--metadata-file=metadata.yaml" if os.path.exists("metadata.yaml") else "-M"]
        meta = [m for m in meta if m != "-M"]
        for ext, args in {
            "docx": [], "epub": ["--epub-cover-image=cover.jpg"],
        }.items():
            subprocess.run(["pandoc", OUT, "-o", f"book.{ext}", *meta, *args], check=False)
        subprocess.run(["pandoc", OUT, "-o", "book.pdf", *meta,
                        "--pdf-engine=weasyprint", "--css=style.css"], check=False)
        print("build attempted: book.docx book.epub book.pdf")

if __name__ == "__main__":
    main()