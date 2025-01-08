import pandas as pd

# Load the second Excel file (the search key)
search_file = "search_file.xlsx"
search_sheet = "Sheet1"  # Update if necessary
search_column = "SearchColumn"  # Column name containing search keys

search_df = pd.read_excel(search_file, sheet_name=search_sheet)
search_keys = search_df[search_column].tolist()

# Load the first Excel file (the one to search in)
input_file = "input_file.xlsx"
output_file = "output_file.xlsx"  # File to save the results
writer = pd.ExcelWriter(output_file, engine='openpyxl')

# Iterate over all sheets in the first Excel file
sheets_data = pd.ExcelFile(input_file)
for sheet_name in sheets_data.sheet_names:
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    
    # Assuming we're searching in one specific column
    search_in_column = "ColumnToSearch"  # Update with the correct column name
    
    # Filter rows where the column matches the search keys
    if search_in_column in df.columns:
        matched_rows = df[df[search_in_column].isin(search_keys)]
        if not matched_rows.empty:
            # Write matched rows to the output Excel
            matched_rows.to_excel(writer, sheet_name=sheet_name, index=False)

# Save the results
writer.close()
print(f"Matching rows saved to {output_file}")
