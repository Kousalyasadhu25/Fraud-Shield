import pdfplumber
from docx import Document
import easyocr
import os


# ==========================
# OCR Setup
# ==========================

reader = easyocr.Reader(
    ['en'],
    gpu=False
)



# ==========================
# Extract PDF Text
# ==========================

def extract_pdf(file_path):

    text = ""


    with pdfplumber.open(file_path) as pdf:


        for page in pdf.pages:


            page_text = page.extract_text()


            if page_text:

                text += page_text + "\n"



    return text.strip()




# ==========================
# Extract DOCX Text
# ==========================

def extract_docx(file_path):


    document = Document(file_path)


    text = ""


    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"



    return text.strip()




# ==========================
# Extract TXT Text
# ==========================

def extract_txt(file_path):


    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:


        return file.read().strip()




# ==========================
# Extract Image Text
# ==========================

def extract_image(file_path):


    result = reader.readtext(
        file_path
    )


    text = ""


    for item in result:


        text += item[1] + " "



    return text.strip()




# ==========================
# Main Extract Function
# ==========================

def extract_text(file_path):


    extension = os.path.splitext(
        file_path
    )[1].lower()



    if extension == ".pdf":

        return extract_pdf(file_path)



    elif extension == ".docx":

        return extract_docx(file_path)



    elif extension == ".txt":

        return extract_txt(file_path)



    elif extension in [

        ".png",
        ".jpg",
        ".jpeg",
        ".webp"

    ]:

        return extract_image(file_path)



    else:

        return ""
