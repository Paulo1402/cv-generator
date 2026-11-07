#!/usr/bin/env python3
"""Generate a PDF CV from a YAML document and an HTML/CSS template."""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML

BASE_DIR = Path(__file__).resolve().parent


def generate(data_path: Path, output_path: Path) -> None:
    with data_path.open('r', encoding='utf-8') as stream:
        cv = yaml.safe_load(stream)

    if not isinstance(cv, dict) or not cv.get('name'):
        raise ValueError('Your YAML data must contain a nonempty "name".')

    env = Environment(
        loader=FileSystemLoader(BASE_DIR / 'templates'),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    html = env.get_template('cv.html').render(cv=cv)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(BASE_DIR / 'templates')).write_pdf(str(output_path))
    print(f'Created {output_path.resolve()}')


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate a PDF CV using YAML data.')
    parser.add_argument('--data', type=Path, default=BASE_DIR / 'cv.yaml')
    parser.add_argument('--output', type=Path, default=BASE_DIR / 'output' / 'cv.pdf')
    args = parser.parse_args()
    generate(args.data.resolve(), args.output.resolve())


if __name__ == '__main__':
    main()
