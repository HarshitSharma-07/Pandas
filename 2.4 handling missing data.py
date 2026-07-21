import pandas as pd

data={"name":["reena",None,"tina","seema","geeta","ritu","neetu","jeetu",],
      "class":[1,None,3,4,5,6,7,8],
      "roll_num":[23,None,25,26,27,28,29,30],
      "internship":[25000,None,10000,12890,14520,53320,12430,43542]}

df=pd.DataFrame(data)

print(df)


print(df.isnull())


print(df.isnull().sum())



# now how to handle this missing data??
# there are two options:
# 1. to remove the missing data
#              OR
# 2. to fill the missing data with some other data




# 1:


# print(df.dropna(inplace=False))


# 2:


# print(df.fillna(0,inplace=False))


print(df['class'].fillna(df['class '].mean(), inplace=False))


