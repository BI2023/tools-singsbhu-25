import pandas as pd

# File paths
input_file = "input_file.xlsx"  # File with multiple sheets
search_file = "search_file.xlsx"  # File with search criteria
output_file = "output_file.xlsx"  # File to save the results

# Load the search file
search_df = pd.read_excel(search_file)
# Columns: SheetName, SearchColumn1, SearchColumn2
sheet_column = "SheetName"  # Column with sheet names
search_column1 = "SearchColumn1"  # First search column
search_column2 = "SearchColumn2"  # Second search column

# Create an Excel writer for the output
writer = pd.ExcelWriter(output_file, engine='openpyxl')

# Iterate through rows in the search file
for _, row in search_df.iterrows():
    sheet_name = row[sheet_column]
    value1 = row[search_column1]
    value2 = row[search_column2]

    try:
        # Load the target sheet from the input file
        df = pd.read_excel(input_file, sheet_name=sheet_name)

        # Assuming we're searching in specific columns in the target sheet
        target_column1 = "ColumnToSearch1"  # Update with correct column name
        target_column2 = "ColumnToSearch2"  # Update with correct column name

        # Check if both columns exist
        if target_column1 in df.columns and target_column2 in df.columns:
            # Filter rows matching both criteria
            matched_rows = df[(df[target_column1] == value1) & (df[target_column2] == value2)]
            
            if not matched_rows.empty:
                # Write matched rows to the output Excel
                output_sheet_name = f"{sheet_name}_matches"
                matched_rows.to_excel(writer, sheet_name=output_sheet_name, index=False)
    except Exception as e:
        print(f"Error processing sheet '{sheet_name}': {e}")

# Save the results
writer.close()
print(f"Matching rows saved to {output_file}")
