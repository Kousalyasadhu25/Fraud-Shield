from src.image_processor import extract_text_from_image
from src.predict import predict_message


file = "test_scam.jpeg"

text = extract_text_from_image(file)

print("\nExtracted Text:")
print(text)


result = predict_message(text)

print("\nFraudShield Result:")
print(result)