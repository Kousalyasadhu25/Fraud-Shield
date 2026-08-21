import pandas as pd

# ==========================
# Load Merged Dataset
# ==========================
df = pd.read_csv("merged/fraudshield_dataset.csv")

# ==========================
# Rename Categories
# ==========================
df["category"] = df["category"].replace({
    "safe": "Safe",
    "Child Scam": "Child Game Scam",
    "Financial & Phishing Scams": "Phishing Scam"
})

# ==========================
# Save Updated Dataset
# ==========================
df.to_csv("merged/fraudshield_dataset.csv", index=False)

# ==========================
# Display Results
# ==========================
print("\n✅ Categories updated successfully!\n")

print("Updated Category Distribution:")
print(df["category"].value_counts())