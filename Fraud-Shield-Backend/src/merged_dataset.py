import pandas as pd
import glob
import os

# Folder containing CSV files
folder = "dataset"

# Get all CSV files
csv_files = glob.glob(os.path.join(folder, "*.csv"))

print(f"Found {len(csv_files)} CSV files.")

# Read and merge all files
dfs = []

for file in csv_files:
    print(f"Reading: {os.path.basename(file)}")
    df = pd.read_csv(file)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

# Save merged file
merged_df.to_csv("fraudshield_dataset.csv", index=False)

print("\n✅ Merge completed successfully!")
print(f"Total rows: {len(merged_df)}")
print("Saved as: fraudshield_dataset.csv")