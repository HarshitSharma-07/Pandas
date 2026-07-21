import pandas as pd

data={"name":["reena","meena","tina","seema","geeta","ritu","neetu","jeetu",],
      "Class":[1,2,3,4,5,6,7,8],
      "roll_num":[23,24,25,26,27,28,29,30],
      "internship":[25000,30000,10000,12890,14520,53320,12430,43542]}
df=pd.DataFrame(data)
print(df)
print(f"data shape={df.shape}")
print(f"data columns={df.columns}")
print(f"rows: {df.index}")
print(f"number of rows: {len(df.index)}")

