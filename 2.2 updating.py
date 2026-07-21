import pandas as pd

data={"name":["reena","meena","tina","seema","geeta","ritu","neetu","jeetu",],
      "class":[1,2,3,4,5,6,7,8],
      "roll_num":[23,24,25,26,27,28,29,30],
      "internship":[25000,30000,10000,12890,14520,53320,12430,43542]}

df=pd.DataFrame(data)


# df.loc[0,"internship"]=45000
print(df)


# can also print rows using df.loc[[0,1,3,4]]


df['class']=df["class"]+2
print(df)