import pandas as pd
file = 'example.xls'
xl = pd.ExcelFile(file)
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet1')
