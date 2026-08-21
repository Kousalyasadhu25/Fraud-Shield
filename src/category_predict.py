import joblib

# Load trained model and vectorizer
model = joblib.load("models/fraud_category_detector.pkl")
vectorizer = joblib.load("models/category_vectorizer.pkl")


def predict_category(message):
    """
    Predicts fraud category and confidence.
    Returns:
        category (str)
        confidence (float)
    """

    # Convert text into TF-IDF features
    message_vector = vectorizer.transform([message])

    # Predict category
    category = model.predict(message_vector)[0]

    # Confidence (only works for models supporting predict_proba)
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(message_vector)[0]
        confidence = max(probabilities) * 100
    else:
        confidence = 0.0

    return category, round(confidence, 2)


# Testing
if __name__ == "__main__":

    while True:

        text = input("\nEnter Message (type 'exit' to quit): ")

        if text.lower() == "exit":
            break

        category, confidence = predict_category(text)

        print("\n==============================")
        print(" FRAUD CATEGORY DETECTION")
        print("==============================")

        print(f"Category   : {category}")
       