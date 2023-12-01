
#kindly download:
#Download the Dataset
#Download the dataset to your local computer in the project directory of your choice.
#results.csv includes the following columns:
#date - date of the match home_team - the name of the home team away_team - the name of the away team home_score - full-time home team score including extra time, not including penalty-shootouts away_score - full-time away team score including extra time, not including penalty-shootouts tournament - the name of the tournament city - the name of the city/town/administrative unit where the match was played country - the name of the country where the match was played neutral - TRUE/FALSE column indicating whether the match was played at a neutral venue
#Note on team and country names:
#For home and away teams the current name of the team has been used. For example, when in 1882 a team who called themselves Ireland played against England, in this dataset, it is called Northern Ireland because the current team of Northern Ireland is the successor of the 1882 Ireland team. This is done so it is easier to track the history and statistics of teams.
#For country names, the name of the country at the time of the match is used. So when Ghana played in Accra, Gold Coast in the 1950s, even though the names of the home team and the country don't match, it was a home match for Ghana. This is indicated by the neutral column, which says FALSE for those matches, meaning it was not at a neutral venue.

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#Reading the Dataset
df = pd.read_csv('results.csv')#Read the dataset into a Pandas DataFrame!


#Read the dataset into the Pandas DataFrame!
#Does the dataset include any missing values? If so, delete the missing value entries!
#Hint: Pandas can do that with one line of code!
df = df.replace(r'^\s*$', np.nan, regex=True)
df = df.dropna()




#Exploring the Dataset
#Answer the following questions about the dataset using Python commands:
#How many tuples are there in the dataset?
numTuples = len(df)
print("total tuples:",numTuples)


#How many tournaments are there in the dataset?
num_tournaments = len(df['tournament'].unique())
print("total types of tournament",num_tournaments)




#Hint: Each question should require few lines of code!
#Convert and Deduce
#Convert the column date to timestamps!


df['date'] = df['date'].apply(lambda x: pd.Timestamp(x))


#Find out how many matches in the dataset were played in 2018.
#Hint: Use the date column.

count = sum(  df['date'].dt.year == 2018)
print("Matches played in 2018",count)


#Team Statistics
#Calculate how many times the home team won, lost, or had a draw.
home_won = sum (df['home_score']>df['away_score'])
print("home won:",home_won)

home_lost = sum (df['away_score']>df['home_score'])
print("home lost:",home_lost)

home_draw = sum (df['away_score']==df['home_score'])
print("home draw:",home_draw)



#Visualization
#Plot the numbers extracted from step 5 in a pie chart.

data = [home_won, home_lost, home_draw]
labels = ['home_won', 'home_lost', 'home_draw']
plt.pie(data, labels = labels, autopct='%.0f%%')
plt.show()



#Plot the neutral column as a pie chart.
#Hint: Try to Visualize the neutral column Using Pandas (Only one line of code).



data1 = [sum(df['neutral'].values == False) , sum(df['neutral'].values == True)]
label1 = ["False","True"]
plt.pie(data1, labels= label1, autopct='%.0f%%')
plt.show()



df