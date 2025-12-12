import pandas as pd
import matplotlib.pyplot as plt
#loading dataset which has been taken from kaggle
df = pd.read_csv('sales_data.csv')

# cleaning columns names
df.columns = df.columns.str.strip().str.lower() #removing extra spaces and converting uppercase to lowercase
 
#showing columns
print("----Columns in file----")
print(df.columns)

#correct month order
monthorder = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]

#grouping by month and summing the sales
monthly = df.groupby("month")["sales"].sum().reset_index() #index reseting and summing of sales

#months sorting
monthly["month"] = pd.Categorical(monthly["month"], categories=monthorder, ordered=True) #correct the proper month order
monthly = monthly.sort_values("month")

#plotting the line graph
plt.figure(figsize=(10,5))
plt.plot(monthly["month"], monthly["sales"], marker='o', linewidth=2)

plt.title("Monthly Sales Trend") #title of graph
plt.xlabel("Month") #x axis label 
plt.ylabel("Sales") #y axis label
plt.grid(True) #lines of grid
plt.tight_layout() #automatically adjust the labels or titles
plt.show() #display the graph
