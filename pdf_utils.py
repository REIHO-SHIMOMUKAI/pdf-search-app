import pdfplumber

def extract_text(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def highlight(text, keyword):
    if not keyword:
        return text
    return text.replace(keyword, f"<mark>{keyword}</mark>")
