import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
movies_file_path = 'Dataset/Movies.csv'
movies_data = pd.read_csv(movies_file_path)

# Combine runtime_hour and runtime_min into total runtime in minutes
movies_data['total_runtime_min'] = movies_data['runtime_hour'] * 60 + movies_data['runtime_min']

# Filter movies with runtime less than 90 minutes (1 hour 30 minutes)
filtered_movies = movies_data[movies_data['total_runtime_min'] < 90]

# Ensure 'filtered_movies' is a pandas DataFrame
if not isinstance(filtered_movies, pd.DataFrame):
    filtered_movies = pd.DataFrame(filtered_movies)

# Convert 'genres' back to a pandas Series if needed
if isinstance(filtered_movies['genres'], (list, np.ndarray)):
    filtered_movies['genres'] = pd.Series(filtered_movies['genres'])

# Ensure the 'genres' column is a proper string column
filtered_movies['genres'] = filtered_movies['genres'].fillna('').astype(str)

# Split genres into lists
filtered_movies['genres_split'] = filtered_movies['genres'].str.split(', ')

# Explode the genres into separate rows for each movie
exploded_genres = filtered_movies.explode('genres_split')

# Group by genres and calculate the average user score
genre_avg_score = exploded_genres.groupby('genres_split').agg(
    average_user_score=('user_score', 'mean')
).reset_index()

# Sort by average user score
genre_avg_score = genre_avg_score.sort_values(by='average_user_score', ascending=False)

# Plot the average user score by genre
plt.figure(figsize=(12, 6))
plt.barh(genre_avg_score['genres_split'], genre_avg_score['average_user_score'], color='skyblue')
plt.xlabel('Average User Score')
plt.ylabel('Genre')
plt.title('Average User Score by Genre (Movies < 1h 30m)')
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.show()
