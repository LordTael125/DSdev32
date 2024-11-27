import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Dataset/Movies.csv'
movies_data = pd.read_csv(file_path)

# Combine runtime_hour and runtime_min into total runtime in minutes
movies_data['total_runtime_min'] = movies_data['runtime_hour'] * 60 + movies_data['runtime_min']

# Ensure numeric columns are valid and exist
numeric_columns = ['user_score', 'vote_count', 'total_runtime_min']

# Drop non-numeric columns and handle missing values
numeric_data = movies_data[numeric_columns].select_dtypes(include=['number']).dropna()

# Compute the correlation matrix
correlation_matrix = numeric_data.corr()

# Display the correlation matrix
print(correlation_matrix)
# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
