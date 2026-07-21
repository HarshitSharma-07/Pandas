import pandas as pd

df1=pd.DataFrame({"name":["Avinash","Abhishek","Rampal","Kaluram"],
                  "Job":["Civil Engineer","Accountant","Hr","Call centre"]})


df2=pd.DataFrame({"name":["Pradeep","Subhash","Atul","Rajendra"],
                  "Job":["Business","Football Player","Lawyer","DSP"]})


# ignore index resets the indices whereas when it's false, the indices remains the same
concatenated_df=pd.concat([df1,df2],ignore_index=True) # axis=0 by default
print(concatenated_df)



concatenated_df=pd.concat([df1,df2],axis=1,ignore_index=False) # axis=0 by default
print(concatenated_df)
