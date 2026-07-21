import pandas as pd
"""
to find values like mean,median,sum,min,max etc...
"""


data={"Name":["Harshit","Chaman","Chunmun","Mummy","Papa"],
      "Salary":[10000,13500,20000,30000,40000],
      "Age":[18,18,20,50,50]}

df=pd.DataFrame(data)

avg_salary=df["Age"].mean()
print(avg_salary)