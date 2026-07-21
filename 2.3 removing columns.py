import pandas as pd

data={"name":["reena","meena","tina","seema","geeta","ritu","neetu","jeetu",],
      "class":[1,2,3,4,5,6,7,8],
      "roll_num":[23,24,25,26,27,28,29,30],
      "internship":[25000,30000,10000,12890,14520,53320,12430,43542]}

df=pd.DataFrame(data)

df.insert(3,"age",[25,35,34,24,45,42,23,56])
print(df)


print("modified dataframe")



df.drop(columns=["age","class"],inplace=True)# inplace=True means to modify the real dataframe,inplace=false== get new dataframe
print(df)
