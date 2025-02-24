import pandas as pd
df = pd.read_csv('your_file.csv')  # Load your CSV or data file

# Creating a DataFrame from a dictionary

# Explanation: Creating a DataFrame using a dictionary with multiple columns

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)  # Converts dictionary into a DataFrame
print(df)
