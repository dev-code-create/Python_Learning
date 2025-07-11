import pandas as pd

df = pd.read_csv("Students.csv")
print(df)

print(df.head())    # First 5 rows
print(df.tail())    # Last 5 rows

print(df["Marks"].mean())     # Average marks
print(df["Marks"].max())      # Highest marks
print(df["Marks"].min())      # Lowest marks

top_students = df[df["Marks"] > 90]
print(top_students)