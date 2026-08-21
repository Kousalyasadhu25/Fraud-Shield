import easyocr


# ==========================
# OCR Setup
# ==========================

reader = easyocr.Reader(
    ['en'],
    gpu=False
)



# ==========================
# Extract Text From Image
# ==========================

def extract_text_from_image(image_path):


    result = reader.readtext(
        image_path
    )


    text = ""


    for detection in result:


        # detection format:
        # [bounding_box, text, confidence]

        text += detection[1] + " "



    return text.strip()




# ==========================
# Test OCR Locally
# ==========================

if __name__ == "__main__":


    image_path = input(
        "Enter image path: "
    )


    extracted_text = extract_text_from_image(
        image_path
    )


    print("\n========== OCR OUTPUT ==========")

    print(extracted_text)