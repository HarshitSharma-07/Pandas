import pandas as pd
import numpy as np

n = 30
data=df = pd.DataFrame({
    "Region": np.random.choice(["North", "South", "East", "West"], n),
    "Product": np.random.choice(["Laptop", "Phone", "Tablet", "Monitor"], n),
    "Salesperson": np.random.choice(["Alice", "Bob", "Charlie", "David", "Eva"], n),
    "Month": np.random.choice(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], n
    ),
    "Sales": np.random.randint(100, 1000, n),
    "Profit": np.random.randint(20, 300, n),
})

df=pd.DataFrame(data)

pivoted_df=df.pivot_table(index=["Product","Salesperson"],columns="Month",values=["Sales","Profit"],aggfunc="mean")
print(pivoted_df)


# makes the data more readable
