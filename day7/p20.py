import pandas as pd
df = pd.read_csv('your_file.csv')  # Load your CSV or data file

# Filtering rows in Pandas based on a condition

# Explanation: Using boolean indexing to filter rows where Age > 25

filtered_df = df[df['Age'] > 25]  # Selects rows where Age > 25
print(filtered_df)
