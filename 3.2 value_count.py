import pandas as pd

data={"name":["reena",None,"tina","seema","reena","tina","neetu","seema",],
      "class":[1,None,3,4,5,6,7,8],
      "roll_num":[23,None,25,26,27,28,29,30],
      "internship":[25000,None,10000,12890,14520,53320,12430,43542]}


df=pd.DataFrame(data)
print(df["name"].value_counts())