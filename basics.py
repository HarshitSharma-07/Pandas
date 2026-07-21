# Series-one dimensional labelled array that can hold any data type
# dataframe-2d labelled data structure, it consist of rows and columns
# 2 types of encoding-latin1 or utf-8(for csv files)
import pandas as pd
df=pd.read_json('sample_Data.json')
print(df)

# to read data from clouds, use gcsfs library