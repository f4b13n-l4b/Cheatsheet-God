#!/usr/bin/env python3
"""
PDF Generator for Cheatsheet-God
Converts text cheatsheets to PDF format
"""

import os
import sys
import glob
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def generate_pdf_from_text(text_file, output_file=None):
    """
    Generate a PDF from a text file.
    
    Args:
        text_file: Path to the input text file
        output_file: Path to the output PDF file (optional)
    """
    if output_file is None:
        output_file = text_file.replace('.txt', '.pdf')
    
    # Read the text file
    try:
        with open(text_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {text_file}: {e}")
        return False
    
    # Create PDF
    try:
        doc = SimpleDocTemplate(
            output_file,
            pagesize=letter,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.75*inch,
            bottomMargin=0.5*inch
        )
        
        # Container for the 'Flowable' objects
        elements = []
        
        # Define styles
        styles = getSampleStyleSheet()
        
        # Create a custom style for code/preformatted text
        code_style = ParagraphStyle(
            'Code',
            parent=styles['Code'],
            fontName='Courier',
            fontSize=8,
            leading=10,
            leftIndent=0,
            rightIndent=0,
            alignment=TA_LEFT,
            spaceBefore=0,
            spaceAfter=0
        )
        
        # Add title
        title = os.path.basename(text_file).replace('.txt', '').replace('Cheatsheet_', '')
        title_style = styles['Title']
        elements.append(Paragraph(title, title_style))
        elements.append(Spacer(1, 0.2*inch))
        
        # Split content into lines and process
        lines = content.split('\n')
        
        # Group consecutive non-empty lines together
        current_block = []
        for line in lines:
            if line.strip():
                current_block.append(line)
            else:
                if current_block:
                    # Join the block and add as preformatted text
                    block_text = '\n'.join(current_block)
                    try:
                        pre = Preformatted(block_text, code_style)
                        elements.append(pre)
                    except Exception as e:
                        # If preformatted fails, try as regular paragraph
                        try:
                            elements.append(Paragraph(block_text.replace('\n', '<br/>'), styles['Normal']))
                        except:
                            pass
                    current_block = []
                elements.append(Spacer(1, 0.1*inch))
        
        # Don't forget the last block
        if current_block:
            block_text = '\n'.join(current_block)
            try:
                pre = Preformatted(block_text, code_style)
                elements.append(pre)
            except Exception as e:
                try:
                    elements.append(Paragraph(block_text.replace('\n', '<br/>'), styles['Normal']))
                except:
                    pass
        
        # Build PDF
        doc.build(elements)
        print(f"✓ Generated: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error generating PDF for {text_file}: {e}")
        return False


def main():
    """Main function to generate PDFs from all text cheatsheets."""
    # Get all text files starting with "Cheatsheet_"
    text_files = glob.glob("Cheatsheet_*.txt")
    
    if not text_files:
        print("No cheatsheet text files found.")
        return
    
    print(f"Found {len(text_files)} cheatsheet(s) to convert.")
    print("-" * 50)
    
    success_count = 0
    fail_count = 0
    
    for text_file in sorted(text_files):
        if generate_pdf_from_text(text_file):
            success_count += 1
        else:
            fail_count += 1
    
    print("-" * 50)
    print(f"Completed: {success_count} successful, {fail_count} failed")
    
    if fail_count == 0:
        print("\n✓ All cheatsheets converted successfully!")
    

if __name__ == "__main__":
    main()
