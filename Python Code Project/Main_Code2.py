# Import the required libraries
import pandas as pd

def read_excel_file(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_name}' does not exist in the folder '{folder_path}'.")
    
    df = pd.read_excel(file_path)  # Read the Excel file into a DataFrame
    return df

def generate_nested_pivot_table(df, index_cols, column_cols, values_col, agg_func='sum'):
    pivot_table = pd.pivot_table(df, values=values_col, index=index_cols, columns=column_cols, aggfunc=agg_func)
    return pivot_table,dataframe

# Define the folder path and file name
absolute_path = "./ML_Pivot_Automation"
folder_path = os.path.abspath(absolute_path)
file_name = 'InputFile.xlsx'  # Replace with the actual Excel file name

# Define the index columns, column columns, and values column
index_columns = ['Department', 'First Name']  # Replace with the actual columns to be used as index
column_columns = ['Position']  # Replace with the actual columns to be used as columns
values_column = 'Last Name'  # Replace with the actual column for values

try:
    dataframe = read_excel_file(folder_path, file_name)

    # Apply the lambda function to check conditions and update the last name in a new column
    dataframe['New Column'] = dataframe.apply(lambda x: x['Last Name'] if x['Department'] == 'Engineering' and x['First Name'] == 'Michael' else None, axis=1)

    pivot_table = generate_nested_pivot_table(dataframe, index_columns, column_columns, values_column)
    print(pivot_table)
    print(dataframe)
except FileNotFoundError as e:
    print(e)


