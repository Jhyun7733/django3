import pdfplumber

pdf = pdfplumber.open("아뱅.pdf")

for i in pdf.pages:
    print(i.extract_text())