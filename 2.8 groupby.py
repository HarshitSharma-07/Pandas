import pandas as pd

data={"Name":["Pinky","Bablu","Tina","Raveena","Hijda","Ram","Lakshman","Gudia"],
      "Age":[43,23,54,75,54,75,23,43],
      "Salary":[25000,45620,68150,94680,56394,39593,33449,34840],
      "Room_No":[12,42,35,55,32,12,35,55]}
df=pd.DataFrame(data)
grouped=df.groupby("Age")["Salary"].sum()
print(grouped)


# Now Multiple grouping

# multi_grouped=df.groupby(["Age","Room_No"])["Salary"].sum()
# print(multi_grouped)