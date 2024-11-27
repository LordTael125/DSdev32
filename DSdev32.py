# Program to get a movie recommendation

# Necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Class that provide methods for data analysis and display and manipulation
class moviesData :

    # calling the data from the csv file
    def __init__(self) :

        print("Connecting to the Dataset\n")
        self.Movies = pd.read_csv("src/Dataset/Movies.csv")
        print("Dataset connected and loaded into class")
        print("Displaying the first 10 data from each table\n")
        self.First10Data()


    #displaying all the data
    def First10Data(self) :
        print("The data of Movies")
        print(self.Movies.head(10))

    #giving a analysis
    def genreAnalyse(self) :

        user_time = int(input("Enter maximum movie lenght in minutes (1hr : 60m, 2hr : 120 ,...): "))

        movies_data = self.Movies

        # Combine runtime_hour and runtime_min into total runtime in minutes
        movies_data['total_runtime_min'] = movies_data['runtime_hour'] * 60 + movies_data['runtime_min']

        # Filter movies with runtime less than 90 minutes (1 hour 30 minutes)
        filtered_movies = movies_data[movies_data['total_runtime_min'] < user_time]

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


    def CorrelationAnalysis(self) :

        movies_data = self.Movies
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


    def MoviesRefer(self) :

        movies_data = self.Movies

        # Function to get top 5 movies for a specific genre
        def get_top_movies_by_genre(genre, data, top_n=5):
            # Filter movies that contain the given genre
            genre_filtered = data[data['genres'].str.contains(genre, case=False, na=False)]

            # Sort movies by user score (descending) and vote count (descending)
            sorted_movies = genre_filtered.sort_values(by=['user_score', 'vote_count'], ascending=[False, False])

            # Get the top N movies
            top_movies = sorted_movies.head(top_n)[['title', 'user_score', 'vote_count', 'release_date']]
            return top_movies


        user_genre = input("Enter a genre to see the top 5 movies: ").strip()
        top_movies = get_top_movies_by_genre(user_genre, movies_data)

        # Display the results
        print(f"\nTop 5 Movies in the '{user_genre}' Genre:")
        print(top_movies)

# Script to control program flow
class mainScript :

    #the main script to control the program
    def __init__(self) :

        print("#","-"*150,"#")
        print("This is a Film recommendation program which recommends a movie based on the basis of genre and user scores around the globe.")
        print("#","-"*150,"#")
        self.Data1 = moviesData()
        print("#","-"*150,"#")
        self.menu()

    # Main menu for the program
    def menu(self) :
        print("#","-"*150,"#")
        print("What data do you want to see : ")
        print("""
            1.) Top genres based on user review score
            2.) Top recommended Movies
            3.) Basis/Criteria for which the data has been filtered inn the form of a heat map
            4.) Exit the program """)
        print("#","-"*150,"#")
        self.Decision()

    # function to control decision flow
    def Decision(self) :
        flow = int(input("Enter the index for the search :"))

        if (flow == 1) :
            print("Displaying top genres based on user review score")
            print("#","-"*150,"#")
            self.Data1.genreAnalyse()
            print("#","-"*150,"#")

        elif (flow == 2) :
            print("Displaying top recommended movies based on user review score and genre user wants too see")
            print("#","-"*150,"#")
            self.Data1.MoviesRefer()
            print("#","-"*150,"#")

        elif (flow == 3) :
            print("Displaying criteria for data filtering in the form of heat map")
            print("#","-"*150,"#")
            self.Data1.CorrelationAnalysis()
            print("#","-"*150,"#")

        elif (flow == 4) :
            while (True) :
                exit = input("Are you sure (y/n) : ")
                if (exit == 'y' or exit == 'Y') :
                    print("Exiting the program :")
                    print("#","-"*150,"#")
                    quit();
                elif (exit == 'n' or exit == 'N') :
                    print("OK.\nDirecting back to menu")
                    self.menu()
                    print("#","-"*150,"#")
                else :
                    print("Error : 40021e\nNot a proper response !!\nPlease confirm again")
                    print("#","-"*150,"#")

        else :
            print("You have entered a wrong index number")
            print("#","-"*150,"#")


        self.menu()


main = mainScript()
