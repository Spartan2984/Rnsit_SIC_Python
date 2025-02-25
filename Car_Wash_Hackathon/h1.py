'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = (r"D:\Learning\Python\SIC-CP\Rnsit_SIC_Python\Car_Wash_Hackathon\car_wash_datasetcsv.csv")
df = pd.read_csv(file_path)

# Convert 'Visit Date' to datetime
df['Visit Date'] = pd.to_datetime(df['Visit Date'])
df['Day of Week'] = df['Visit Date'].dt.day_name()
df['Month'] = df['Visit Date'].dt.month_name()

### 1. Total Washes Completed (Per Day/Week/Month) ###

daily_washes = df.groupby(df['Visit Date'].dt.date).size()
weekly_washes = df.groupby(df['Visit Date'].dt.to_period('W')).size()
monthly_washes = df.groupby(df['Visit Date'].dt.to_period('M')).size()

# Plotting Daily Washes
plt.figure(figsize=(12,5))
daily_washes.plot(title='Daily Car Wash Trend', color='blue')
plt.xlabel('Date')
plt.ylabel('Total Washes')
plt.show()

# Plotting Weekly Washes
plt.figure(figsize=(10,5))
weekly_washes.plot(kind='bar', color='green', title='Weekly Car Wash Trend')
plt.xlabel('Week')
plt.ylabel('Total Washes')
plt.show()

# Plotting Monthly Washes
plt.figure(figsize=(10,5))
monthly_washes.plot(kind='bar', color='orange', title='Monthly Car Wash Trend')
plt.xlabel('Month')
plt.ylabel('Total Washes')
plt.show()

### 2. Most Popular Services ###

service_counts = df['Service'].value_counts()

# Bar chart for service popularity
plt.figure(figsize=(8,5))
sns.barplot(x=service_counts.values, y=service_counts.index, palette='viridis')
plt.title('Most Popular Car Wash Services')
plt.xlabel('Number of Washes')
plt.ylabel('Service Type')
plt.show()

### 3. Peak Days ###

day_washes = df.groupby('Day of Week').size()
plt.figure(figsize=(8,5))
sns.barplot(x=day_washes.index, y=day_washes.values, palette='coolwarm')
plt.title('Car Washes Per Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Washes')
plt.xticks(rotation=45)
plt.show()
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Learning\Python\SIC-CP\Rnsit_SIC_Python\Car_Wash_Hackathon\car_wash_datasetcsv.csv")

service_counts = df['Service'].value_counts()

plt.figure(figsize=(10, 6))
service_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Preferred Services', fontsize=16)
plt.xlabel('Service Type', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()