import pandas as pd
from sklearn.model_selection import train_test_split

# Load preprocessed dataset
df = pd.read_excel("data/FraudShield_Preprocessed.xlsx")

# Input (cleaned message)
X = df["clean_message"]

# Target (0 = Safe, 1 = Scam)
y = df["label"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("=" * 50)
print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

print("\nTraining Label Distribution")
print(y_train.value_counts())

print("\nTesting Label Distribution")
print(y_test.value_counts())