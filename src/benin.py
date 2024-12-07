import gdown

# Download the file from Google Drive
url = 'https://drive.google.com/uc?id=1z8ow-PPe3oVDKFpk0e_uVP0Lm4HALYrh'  # Updated URL for direct download
output = 'dataset1.csv'  # Specify the output filename
gdown.download(url, output, quiet=False)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load dataset
data = pd.read_csv(output)

# Summary Statistics
summary_stats = data.describe()
print("Summary Statistics:\n", summary_stats)

# Data Quality Check
missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)

outliers = data[(data['GHI'] < 0) | (data['DNI'] < 0) | (data['DHI'] < 0)]
print("Outliers:\n", outliers)

# Time Series Analysis
data['Timestamp'] = pd.to_datetime(data['Timestamp'])  # Ensure 'Timestamp' is in datetime format

plt.figure(figsize=(12, 6))
plt.plot(data['Timestamp'], data['GHI'], label='GHI')
plt.title('GHI Over Time')
plt.xlabel('Date')
plt.ylabel('GHI')
plt.legend()
plt.show()

# Correlation Analysis
correlation_matrix = data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Wind Analysis
plt.figure(figsize=(10, 6))
sns.histplot(data['WS'], bins=30)
plt.title('Wind Speed Distribution')
plt.xlabel('Wind Speed')
plt.ylabel('Frequency')
plt.show()

# Temperature Analysis
plt.figure(figsize=(10, 6))
sns.scatterplot(x='RH', y='TModA', data=data)
plt.title('Relative Humidity vs Temperature ModA')
plt.xlabel('Relative Humidity')
plt.ylabel('Temperature ModA')
plt.show()

# Histograms and Z-Score Analysis
z_scores = stats.zscore(data[['GHI', 'DNI', 'DHI']])
print("Z-Scores:\n", z_scores)

# Data Cleaning (Example: Dropping rows with any NaN values)
data_cleaned = data.dropna()  # Modify this line based on your cleaning strategy

# Optional: Save cleaned data to a new CSV file
data_cleanedbenin.to_csv('cleaned_data.csv', index=False)
