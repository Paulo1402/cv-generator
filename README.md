# Python CV Generator

A YAML-driven, minimalist two-column resume generator, based on your selected design.
It produces text-selectable A4 PDFs with clickable email, LinkedIn, GitHub and portfolio links.

## Setup

Requires Python 3.13+.

```bash
uv venv .venv
uv sync
```

WeasyPrint may require operating-system libraries such as Pango on some platforms.
See https://doc.courtbouillon.org/weasyprint/stable/first_steps.html if installation fails.

## Generate

```bash
python generate.py
# or
python generate.py --data cv.yaml --output output/paulo-cv.pdf
```

## Customize

- Edit **cv.yaml**: personal details, skills by group, certificates, work experience, projects, education.
- Edit **templates/style.css**: fonts, two-column widths, spacing and visual styling.
- Edit **templates/cv.html**: structure and optional sections.
- Remove any section from YAML to hide it automatically (e.g., `certificates: []`).
- The Courses section is intentionally omitted.

## Notes

The included content is a condensed starting point based on your prior CVs. Review and update the wording, dates, professional title, and certificates before sending it to employers.

Very long content may require multiple pages; if targeting a single-page resume, shorten bullets or select fewer entries rather than shrinking fonts excessively.
