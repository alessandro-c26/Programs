#calculate individual grades for groupwork (given a number of students, a number of students for group and the grade of each group)
#created by alessandro c. - only available for personal uses

from math import comb
from itertools import combinations
import numpy as np
import pandas as pd
import math

students = [] 
maxLengthList = int(input("How many students? "))
studentForGroup = int(input("How many students for group? "))
while len(students) < maxLengthList:
    item = input("Enter Student Name in the List: ")
    students.append(item)
    print(students)

combination = comb(len(students), studentForGroup)
print("Number of groups: ", combination)

groups = []
groups = list(combinations(students, studentForGroup))
print(groups)

grades = []
while len(grades) < combination:
    grade = input("Enter grade for each group: ")
    grades.append(grade)

combined = []
for group in groups:
    for person in group:
        combined.append(person)

combined_grades = []

for grade in grades:
    for group in range(studentForGroup):
        combined_grades.append(float(grade))

array = np.column_stack((combined, combined_grades))

labels = ["student", "sum_grades"]
df = pd.DataFrame(data=array, columns=labels)
df["sum_grades"] = pd.to_numeric(df["sum_grades"])
print(df)

df_count = df.groupby(["student"], as_index=False).count()
divisor = df_count.iloc[0, 1]
print("divisor is: ", divisor)

df_sum = df.groupby(["student"], as_index=False).sum()
df_sum["avg_grade"] = df_sum["sum_grades"] / divisor
df_final = df_sum.sort_values(by=['avg_grade'], ascending=False)

print(df_final)
