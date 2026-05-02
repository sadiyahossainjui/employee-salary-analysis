import pandas as pd

df = pd.read_csv("employee_data.csv")

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Department"] = df["Department"].fillna("Unknown")

df = df.drop_duplicates()

df["Join_Date"] = pd.to_datetime(df["Join_Date"])
df["Year"] = df["Join_Date"].dt.year

print("\nCleaned Data:")
print(df)

print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

print("\nEmployee Count by Department:")
print(df.groupby("Department")["Employee"].count())

print("\nHighest Salary Employee:")
print(df.nlargest(1, "Salary"))
