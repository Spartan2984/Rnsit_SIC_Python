import pandas as pd
df = pd.read_csv('your_file.csv')  # Load your CSV or data file

#Grouping data by Age and calculating mean Salary

# Explanation: Using groupby() to aggregate data and compute mean salary

grouped = df.groupby('Age')['Salary'].mean() 
# Groups by Age and calculates mean salary
print(grouped)

#select avg(salary) as Avg_Salary from employees group by age;