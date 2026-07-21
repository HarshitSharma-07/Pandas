import pandas as pd

#  what is interpolation??
# a method to fill a missing data using previous data. It predicts data using previous data trends




data={"name":["reena",None,"tina","seema","geeta","ritu","neetu","jeetu",],
      "class":[1,None,3,4,5,6,7,8],
      "roll_num":[23,None,25,26,27,28,29,30],
      "internship":[25000,None,10000,12890,14520,53320,12430,43542]}

df=pd.DataFrame(data)

print(df)

print(df.interpolate(method="linear",axis=0,inplace=False))  
print(df)
# methods are basically different ways by which pandas predict the data.
# there are multiple methods like-linear, polynomial, time,quadratic, cubic, nearest etc.


df["roll_num"]=df["roll_num"].interpolate(method="linear")#for a single column
print(df["roll_num"])