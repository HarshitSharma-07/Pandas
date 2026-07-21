# why is it used??
# for ex- you have to take data of years 2024 and year 2025 and find the data of customers who have purchased the product in both years

import pandas as pd

df_customers=pd.DataFrame({"Name":["Ena","Meena","Deeka"],
                 "Customer ID":[2,4,7]})

df_orders=pd.DataFrame({"OrderAmount":[200,321,642],
                 "Customer ID":[2,3,7]})

# also order of dataframe passed also matters

merger_df=pd.merge(df_customers,df_orders,on="Customer ID",how="inner") #inner takes intersection
print(merger_df)


merger_df=pd.merge(df_customers,df_orders,on="Customer ID",how="outer") #outer takes union but puts nan where there is no data
print(merger_df)


merger_df=pd.merge(df_customers,df_orders,on="Customer ID",how="left") #left prints complete left but puts nan where data is not common
print(merger_df)



merger_df=pd.merge(df_customers,df_orders,on="Customer ID",how="right") #right prints complete right but puts nan where data is not common
print(merger_df)