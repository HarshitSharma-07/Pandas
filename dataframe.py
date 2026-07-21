import pandas as pd
dict={
    "Name":["aandu","pandu"],
    "class":[1,2],
    "Rollnum":[25,26]
}

df=pd.DataFrame(dict)
print(df)

df.to_csv("first.csv",index=False)
df.to_excel("firstexcel.xlsx")
df.to_json("output.json",index=False)



# head and tail

# data=pd.read_excel("SampleSuperstore.xlsx",)
# print("first 10 lines of data")
# print(data.head(10))
# print("last 10 lines of data")
# print(data.tail(10))