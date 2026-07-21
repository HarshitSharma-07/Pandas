import pandas as pd
# RangeIndex means no. of rows
# Data columns=no of columns
data=pd.read_excel("SampleSuperstore.xlsx")
print(data)
print(data.info())