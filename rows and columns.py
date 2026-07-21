import pandas as pd
data={"name":["reena","meena","tina","seema","geeta","ritu","neetu","jeetu",],
      "Class":[1,2,3,4,5,6,7,8],
      "roll_num":[23,24,25,26,27,28,29,30],
      "internship":[25000,30000,10000,12890,14520,53320,12430,43542]}

df=pd.DataFrame(data)
print(f"this is a column: \n{df["name"]}")

print(f"and these are multiple columns: \n{df[["name","Class","roll_num"]]}")


# how to print rows??

print("student with intership more than 15000")
row=df[df["internship"]>15000]
print(row)

# filtering rows using multiple conditions

filtered_and=df[(df["Class"]>3) & (df["roll_num"]<29)]
print(filtered_and)


filtered_or=df[(df["internship"]>20000) | (df["Class"]>6)]
print(filtered_or)