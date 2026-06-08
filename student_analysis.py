import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Python\Student-Performance-Analysis\student-mat.csv",
    sep=";",
    encoding="latin1"
)

print(df.head())
print(df.columns)
print("===== DATASET OVERVIEW =====")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATES =====")
print("Duplicates Before:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicates After:", df.duplicated().sum())

print("\n===== AVERAGE FINAL GRADE =====")
avg_grade = df["G3"].mean()
print("Average Final Grade (G3):", round(avg_grade, 2))

print("\n===== STUDENTS SCORING ABOVE 15 =====")
above_15 = df[df["G3"] > 15]
print("Number of Students:", len(above_15))

print("\n===== STUDY TIME VS PERFORMANCE =====")
correlation = df["studytime"].corr(df["G3"])
print("Correlation:", round(correlation, 3))

print("\n===== GENDER-WISE PERFORMANCE =====")
gender_avg = df.groupby("sex")["G3"].mean()
print(gender_avg)


plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=10)
plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["studytime"], df["G3"])
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.savefig("scatterplot.png")
plt.show()


plt.figure(figsize=(8, 5))
gender_avg.plot(kind="bar")
plt.title("Average Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average G3")
plt.savefig("barchart.png")
plt.show()

print("\n===== CONCLUSION =====")

print(f"Average Final Grade: {round(avg_grade,2)}")
print(f"Students scoring above 15: {len(above_15)}")
print(f"Study Time Correlation: {round(correlation,3)}")

if correlation > 0:
    print("Study time has a weak positive relationship with final grades.")
else:
    print("Study time has a negative relationship with final grades.")

if gender_avg["M"] > gender_avg["F"]:
    print("Male students performed slightly better on average.")
else:
    print("Female students performed slightly better on average.")

print("\nAnalysis Complete!")
