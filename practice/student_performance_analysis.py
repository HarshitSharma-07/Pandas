'''Part 1: Explore the data

Try to answer these questions:

How many rows and columns are there?
What are the column names?
What are the data types?
Are there any missing values?
Display the first 5 and last 5 rows.

'''

'''
Part 2: Basic statistics
Average Math marks
Highest Science marks
Lowest English marks
Average attendance
Average study hours
'''


'''
Part 3: Filtering

Find:

Students scoring more than 90 in Math
Students with attendance below 85%
Female students scoring above 90 in Science
Students studying more than 4 hours
'''


import pandas as pd

data=pd.read_csv("C:\programming\python\pandas\practice\student_performance.csv")
df=pd.DataFrame(data)

# PART 1

# print(df.shape)
# print(df.columns)

# print(df.dtypes)

# print(df.isnull().sum())

# print(df.head())

# print(df.tail())


# PART 2


# print(df["Math"].mean())

# print(df["Science"].max()) 
# print(df["English"].max()) 


# print(df["Attendance"].mean()) 


# print(df["Study_Hours"].mean()) 


# PART 3


# print(df[df["Math"]>90]["Name"])
# print(df[df["Math"]>90])



# print(df[df["Attendance"]<85])
# print(df[df["Attendance"]<85]["Name"])



# print(df[(df["Gender"]=="Female") & (df["Science"]>90)])



# print(df[df["Study_Hours"]>4])


# PART 4


# df["Total_Marks"]=df["Math"]+df["Science"]+df["English"]
# print(type(df["Class"]))
print(df.head())