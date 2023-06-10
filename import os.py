import pandas as pd

def generate_pivot_table(input_file, output_file, sheet_name, row_fields, column_fields, value_fields, agg_functions):
    # Read the Excel sheet into a DataFrame
    df = pd.read_excel(input_file, sheet_name=sheet_name)

    # Generate the pivot table
    pivot_table = pd.pivot_table(df, index=row_fields, columns=column_fields, values=value_fields, aggfunc=agg_functions)

    # Save the pivot table to a new Excel file
    pivot_table.to_excel(output_file)

# Specify the input and output file paths
input_file = 'input.xlsx'
output_file = 'output.xlsx'

# Specify the sheet name, row fields, column fields, value fields, and aggregate functions
sheet_name = 'Sheet1'
row_fields = ['RowField1', 'RowField2']
column_fields = ['ColumnField1', 'ColumnField2']
value_fields = ['ValueField1', 'ValueField2']
agg_functions = ['sum', 'mean']

# Generate the pivot table and save it to the output file
generate_pivot_table(input_file, output_file, sheet_name, row_fields, column_fields, value_fields, agg_functions)
