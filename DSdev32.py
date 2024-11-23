# Program to get a movie recommendation

import types
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
#Data1.AllData()

#print(Data1.Movies.columns)

maxlength,DataType,elem = [],[],[]

for x in Data1.Movies :
    print(x)
    elem.extend(x)
    #DataType.extend(Data1.Movies[x].info(type))
    
    
print(DataType)
print()
print(Data1.Movies.info())

temp = list(Data1.Movies['genres'])
label1 = temp.set

print('_'*30)
print(label1)

#plt.plot(label1, label2)
