import pandas as pd

# In drop_duplicates() and duplicated(), the keep parameter does not accept True.
# keep='first'   # Keep first occurrence
# keep='last'    # Keep last occurrence
# keep=False     # Mark/remove all duplicates
data=a={"Name":["Harshit","Chaman","Harshit","Mummy","Chaman"],
      "Salary":[10000,13500,20000,30000,40000],
      "Age":[18,18,20,50,50]}
df=pd.DataFrame(data)
print(df[df.duplicated(subset="Name",keep="first")])

df.drop_duplicates(subset="Name",keep="first",inplace=True)
print(df.duplicated(subset="Name").sum())
