import pandas as pd

# Load the Excel file
input_file = "data.xlsx"
chunk_size = 1000

# Read the file
df = pd.read_excel(input_file)

# Split into chunks
for i in range(0, len(df), chunk_size):
    chunk = df.iloc[i:i + chunk_size]
    chunk.to_excel(f"split_{i // chunk_size + 1}.xlsx", index=False)