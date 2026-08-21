import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_excel("data/FraudShield_Preprocessed.xlsx")

# Features and labels
X = df["clean_message"]
y = df["label"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

# Learn vocabulary from training data
X_train_tfidf = vectorizer.fit_transform(X_train)

# Transform testing data
X_test_tfidf = vectorizer.transform(X_test)

print("=" * 50)
print("Training Shape :", X_train_tfidf.shape)
print("Testing Shape  :", X_test_tfidf.shape)

print("\nFirst 20 Features:\n")
print(vectorizer.get_feature_names_out()[:20])

# Save vectorizer
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("\n✅ TF-IDF Vectorizer Saved Successfully!")