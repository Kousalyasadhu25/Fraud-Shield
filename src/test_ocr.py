import easyocr


reader = easyocr.Reader(['en'])


def extract_text_from_image(image_path):

    result = reader.readtext(image_path)

    text = ""

    for detection in result:
        text += detection[1] + " "

    return text


if __name__ == "__main__":

    image_path = input("Enter image path: ")

    extracted_text = extract_text_from_image(image_path)

    print("\n========== OCR OUTPUT ==========")
    print(extracted_text)