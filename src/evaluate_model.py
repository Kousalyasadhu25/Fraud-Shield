import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# Load dataset
data = pd.read_csv(r"C:\Users\Kousalya\Desktop\module1\merged\fraudshield_dataset.csv")


# Check columns
print(data.head())


# Assuming:
# message = text column
# label = Scam/Safe column

X = data["message"]
y = data["label"]


vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

model = joblib.load("models/scam_detector.pkl")

# Convert text to vectors
X_vector = vectorizer.transform(X)


# Split test data
X_train, X_test, y_train, y_test = train_test_split(
    X_vector,
    y,
    test_size=0.2,
    random_state=42
)


# Prediction
y_pred = model.predict(X_test)


# Metrics

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted"
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted"
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)


print("\n==============================")
print(" FRAUDSHIELD MODEL EVALUATION ")
print("==============================")

print(f"\nAccuracy  : {accuracy*100:.2f}%")
print(f"Precision : {precision*100:.2f}%")
print(f"Recall    : {recall*100:.2f}%")
print(f"F1 Score  : {f1*100:.2f}%")


print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


print("\nClassification Report:")
print(classification_report(y_test, y_pred))