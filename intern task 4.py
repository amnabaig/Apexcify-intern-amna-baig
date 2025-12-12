#task 4
import seaborn as sns #for iris tips or titanic
import pandas as pd #for data analysis and data frames

df = sns.load_dataset("titanic") #loading dataset through seaborn using titanic we can also use tips or iris
#we use titanic here because it contains both numeric and categorical data. best for data analysis task.

#printing 1st five rows of the dataset
print("----First 5 rows----\n")
print(df.head(),"\n")

# printing descriptive statistics of the dataset
print("----Descriptive Statistics----\n")
print(df.describe(include='all'), "\n") #for all row and columns
# print(df.describe(), "\n")

# mean
print("----Mean----\n")
print(df.mean(numeric_only=True), "\n")

#median
print("----Median----\n")
print(df.median(numeric_only=True), "\n")

#minimum
print("----Minimum----\n")
print(df.min(numeric_only=True), "\n")

#maximum
print("----Maximum----\n")
print(df.max(numeric_only=True), "\n")

#standard deviation
print("----Standard Deviation----\n")
print(df.std(numeric_only=True), "\n")

#missing values
print("----Missing Values----\n")
print(df.isnull().sum(), "\n")

