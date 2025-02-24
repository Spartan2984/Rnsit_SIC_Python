import pandas as pd
df = pd.read_csv('your_file.csv')  # Load your CSV or data file

# Checking for missing values in a DataFrame

# Explanation: Using isnull() to check for missing values and count occurrences

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None],
    'Age': [25, None, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
print(df.isnull())  # Identifies missing values
print(df.isnull().sum())  # Counts missing values per column


#Selecting a single column from a DataFrame

# Explanation: Accessing specific columns from the DataFrame

print(df['Name'])  # Access column using dictionary-style indexing
print(df.Age)      # Access column using dot notation
