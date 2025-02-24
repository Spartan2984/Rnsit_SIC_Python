import pandas as pd
df = pd.read_csv('your_file.csv')  # Load your CSV or data file

# Filtering rows where Salary > 50000

# Explanation: Using boolean indexing to filter rows based on Salary column

high_salary = df[df['Salary'] > 50000]  # Filters rows based on Salary
print(high_salary)
