import pdfplumber
import docx

def extract_text(filepath):
    """
    Extracts raw text from a resume file (PDF or DOCX).
    Returns the text as a single string.
    """
    if filepath.endswith('.pdf'):
        return extract_from_pdf(filepath)
    elif filepath.endswith('.docx'):
        return extract_from_docx(filepath)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")


def extract_from_pdf(filepath):
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_from_docx(filepath):
    doc = docx.Document(filepath)
    text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
    return text