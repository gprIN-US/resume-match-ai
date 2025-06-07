import pdfplumber

def extract_text_from_jd(jd_path):
    with pdfplumber.open(jd_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text.strip()
if __name__ == "__main__":
    path = "examples/sample_jd.pdf"
    print(extract_text_from_jd(path))
