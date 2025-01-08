import pandas as pd

search_file = "search_file.xlsx"
search_sheet = "Sheet1"  
search_column = "SearchColumn"  
search_df = pd.read_excel(search_file, sheet_name=search_sheet)
search_keys = search_df[search_column].tolist()


input_file = "input_file.xlsx"
output_file = "output_file.xlsx"  
writer = pd.ExcelWriter(output_file, engine='openpyxl')


sheets_data = pd.ExcelFile(input_file)
for sheet_name in sheets_data.sheet_names:
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    
    
    search_in_column = "ColumnToSearch"  
    
    if search_in_column in df.columns:
        matched_rows = df[df[search_in_column].isin(search_keys)]
        if not matched_rows.empty:
            
            matched_rows.to_excel(writer, sheet_name=sheet_name, index=False)


writer.close()
print(f"Matching rows saved to {output_file}")
