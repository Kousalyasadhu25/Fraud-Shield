import pandas as pd

df=pd.read_csv("data/scam_dataset.csv")

print(df.head())

print("\nLabel distribution:")
print(df['label'].value_counts())

