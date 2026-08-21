import pandas as pd

data = pd.read_csv(r"C:\Users\Kousalya\Desktop\module1\merged\fraudshield_dataset.csv")

print(data["category"].value_counts())