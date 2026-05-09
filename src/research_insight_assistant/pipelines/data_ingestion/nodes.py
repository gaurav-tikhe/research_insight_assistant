from pathlib import Path
from typing import Dict
import pdfplumber

def load_pdfs(data_dir: str) -> Dict[str,str]:
    pdf_texts = {}
    
    for pdf_file in Path(data_dir).glob("*.pdf"):
        text = ""
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        pdf_texts[pdf_file.name] = text
    
    return pdf_texts
