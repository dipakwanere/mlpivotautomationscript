import os
import pandas as pd

def read_excel_file(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_name}' does not exist in the folder '{folder_path}'.")
    
    df = pd.read_excel(file_path)  # Read the Excel file into a DataFrame
    return df

# Example usage
absolute_path = "./ML_Pivot_Automation"
folder_path = os.path.abspath(absolute_path)
file_name = 'InputFile.xlsx'  # Replace with the actual Excel file name

try:
    dataframe = read_excel_file(folder_path, file_name)
    print(dataframe.head())  # Do something with the DataFrame
except FileNotFoundError as e:
    print(e)

# Generate the nested pivot table
pivot_table = pd.pivot_table(df, values='Sales', index=['City', 'Year'], columns=['Product'], aggfunc='sum')

# Display the pivot table
print(pivot_table)