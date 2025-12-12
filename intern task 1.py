# task 1
import pandas as pd#for data analysis and data frames

#dataset loading from kaggle
df = pd.read_csv("StudentsPerformance.csv")

#remane is used to match math, english, science
df = df.rename(columns={
    "math score": "Math",
    "reading score": "English",
    "writing score": "Science"
})

#display few first few rows of data set
print("----First 5 rows----")
print(df.head())

#calculating the average
df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)

# averages
print("\n----Students With Averages----")
print(df)

# Finding the highest average of student
highest_avg_student = df.loc[df["Average"].idxmax()]

print("\n----Top Student/Highest Average of the student----")
print(highest_avg_student)

