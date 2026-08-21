import re

def clean_text(text):
    """
    Clean text for FraudShield ML model.
    """

    # Handle non-string inputs
    if not isinstance(text, str):
        text = str(text)

    # Lowercase
    text = text.lower()

    # Replace URLs
    text = re.sub(r"http\S+|www\.\S+", " URL ", text)

    # Replace email addresses
    text = re.sub(r"\S+@\S+", " EMAIL ", text)

    # Replace phone numbers (10+ digits)
    text = re.sub(r"\b\d{10,}\b", " PHONE ", text)

    # Remove punctuation (keep only letters, digits, spaces)
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text