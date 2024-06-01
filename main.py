import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("texts/*.txt")
pdf = FPDF(orientation ="p", unit ="mm", format = "A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.title()
    #add name to pdf
    pdf.set_font(family ="Times", style ="B", size=16)
    pdf.cell(w=10, h=18, txt=name, ln=1)

    #get content of each text file
    with open(filepath, 'r') as file:
        content=file.read()
    #add text file content to pdf
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)
pdf.output("output.pdf")