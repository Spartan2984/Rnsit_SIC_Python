import pandas as pd
df = pd.read_csv('your_file.csv')  # Load your CSV or data file

# Sorting data by Salary in descending order

# Explanation: Using sort_values() to arrange rows based on Salary

df_sorted = df.sort_values(by='Salary', ascending=False)
print(df_sorted)