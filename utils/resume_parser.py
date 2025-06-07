import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

# Local test
if __name__ == "__main__":
    path = "/Users/prernareddy/resume-match-ai/examples/sample_resume.pdf"

    print(extract_text_from_pdf(path))
