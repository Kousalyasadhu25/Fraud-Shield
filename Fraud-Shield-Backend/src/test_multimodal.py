from file_processor import extract_text
from predict import predict_message

file_path = "test_scam.jpeg"


# Extract text from image
text = extract_text(file_path)


print("\nExtracted Text:")
print(text)


# Send extracted text to FraudShield AI
result = predict_message(text)


print("\n===================")
print("FraudShield Result")
print("===================")

print("Prediction :", result["prediction"])
print("Confidence :", result["confidence"])
print("Risk Level :", result["risk_level"])

print("\nReasons:")

for reason in result["reasons"]:
    print("✓", reason)