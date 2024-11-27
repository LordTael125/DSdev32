import pandas as pd

# Load the dataset
movies_file_path = 'Dataset/Movies.csv'
movies_data = pd.read_csv(movies_file_path)

# Function to get top 5 movies for a specific genre
def get_top_movies_by_genre(genre, data, top_n=5):
    # Filter movies that contain the given genre
    genre_filtered = data[data['genres'].str.contains(genre, case=False, na=False)]

    # Sort movies by user score (descending) and vote count (descending)
    sorted_movies = genre_filtered.sort_values(by=['user_score', 'vote_count'], ascending=[False, False])

    # Get the top N movies
    top_movies = sorted_movies.head(top_n)[['title', 'user_score', 'vote_count', 'release_date']]
    return top_movies

# Example usage
user_genre = input("Enter a genre to see the top 5 movies: ").strip()
top_movies = get_top_movies_by_genre(user_genre, movies_data)

# Display the results
print(f"\nTop 5 Movies in the '{user_genre}' Genre:")
print(top_movies)
