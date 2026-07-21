import pandas as pd

data={"Name":["Harshit","Chaman","Chunmun","Mummy","Papa"],
      "Salary":[10000,13500,20000,30000,40000],
      "Age":[18,18,20,50,50]}
df=pd.DataFrame(data)
print(df)

print("sorted dataframe: ")
print(df.sort_values(by="Age",ascending=False,inplace=False))


# now to sort values according to multiple columns...

print(df.sort_values(by=["Age","Salary"],ascending=False,inplace=False))

print(df.sort_values(by=["Age","Salary"],ascending=[False,True],inplace=False))