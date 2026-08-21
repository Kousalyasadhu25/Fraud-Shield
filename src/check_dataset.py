import pandas as pd

df = pd.read_csv("fraudshield_dataset.csv")

print("=" * 60)
print("FRAUDSHIELD DATASET REPORT")
print("=" * 60)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Messages:")
print(df.duplicated(subset=["message"]).sum())

print("\nLabel Distribution:")
print(df["label"].value_counts())

print("\nCategory Distribution:")
print(df["category"].value_counts())

print("\nFirst 5 Rows:")
print(df.head())