# Program to get a movie recommendation

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


class moviesData : 

    # calling the data from the csv file
    def __init__(self) :
        self.FilmDetails = pd.read_csv("src/Dataset/FilmDetails.csv")
        self.MoreInfo = pd.read_csv("src/Dataset/MoreInfo.csv")
        self.Movies = pd.read_csv("src/Dataset/Movies.csv")
        self.PosterPath = pd.read_csv("src/Dataset/PosterPath.csv")


    #displaying all the data
    def AllData(self) :
        print(self.FilmDetails)
        print(self.MoreInfo)
        print(self.Movies)
        print(self.PosterPath)

    
Data1 = moviesData()
Data1.AllData()

print(Data1.Movies.columns)

