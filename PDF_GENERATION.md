# PDF Generation for Cheatsheet-God

This repository includes a Python script to generate PDF versions of all the text-based cheatsheets.

## Requirements

- Python 3.6 or higher
- reportlab library

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Generate all PDFs

To generate PDF versions of all cheatsheets:

```bash
python3 generate_pdf.py
```

This will create a PDF file for each `.txt` cheatsheet in the repository.

### Generated Files

The script will create PDF files with the same name as the source text files, replacing `.txt` with `.pdf`. For example:
- `Cheatsheet_LinuxPentest.txt` → `Cheatsheet_LinuxPentest.pdf`
- `Cheatsheet_PenTesting.txt` → `Cheatsheet_PenTesting.pdf`

## Features

- Preserves the original formatting of the text files
- Uses monospace font (Courier) for code and command readability
- Automatically adds titles to each PDF based on the filename
- Handles special characters and encoding issues gracefully

## Note

The generated PDFs are formatted with letter size pages and include proper margins for easy printing and reading.
