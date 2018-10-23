import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np


# so this is not the best way to read the data. I made a mistake saving the tweets for each movie in seperate databases.
conn = sqlite3.connect('twitterladyb.db')
c = conn.cursor()
ladyb = pd.read_sql('select * from sentiment', conn)

conn1 = sqlite3.connect('twittercallme.db')
c1 = conn.cursor()
callme = pd.read_sql('select * from sentiment', conn1)

conn2 = sqlite3.connect('twitterdark.db')
c2 = conn.cursor()
darkest = pd.read_sql('select * from sentiment', conn2)

conn3 = sqlite3.connect('twitterDunkirk.db')
c3 = conn.cursor()
dunkirk = pd.read_sql('select * from sentiment', conn3)

conn4 = sqlite3.connect('twittergetout.db')
c4 = conn.cursor()
getout = pd.read_sql('select * from sentiment', conn4)

conn5 = sqlite3.connect('twitterphantom.db')
c5 = conn.cursor()
phantom = pd.read_sql('select * from sentiment', conn5)

conn6 = sqlite3.connect('twitterpost.db')
c6 = conn.cursor()
thepost = pd.read_sql('select * from sentiment', conn6)

conn7 = sqlite3.connect('twittershapewater.db')
c7 = conn.cursor()
shapewater = pd.read_sql('select * from sentiment', conn7)

conn8 = sqlite3.connect('twitterthree.db')
c8 = conn.cursor()
threebills = pd.read_sql('select * from sentiment', conn8)

weekly_track = pd.read_csv('weeklysales.csv')

datafrms = [ladyb, thepost, threebills, shapewater, phantom, getout, dunkirk, darkest, callme]

# movie names as I saved them in the database
m_names = ["ladyb", "thepost", "threebill", "shapeofwater", "phantom", "getout", "dunkirk", "darkest", "callme"]

# in this function, I fix the mess I made before and I save everything in one dataframe.
def prepare_weekly():
    weekly_data = pd.DataFrame(columns=['dates', 'tweet_count', 'sentiment', 'sales', 'movie'])
    for i in range(len(m_names)):
        dataf = datafrms[i]
        dataf['date'] = pd.to_datetime(dataf['date'])
        dataf.sort_values('date', inplace = True)
        dataf.set_index('date', inplace=True)

        weekly_tweets = dataf.resample('w').size()
        weekly_sentiment = dataf.sentiment.resample('w').mean()
        # print(weekly_sentiment)
        weekly_sales = weekly_track[m_names[i]]

        adjusted = []
        for item in weekly_sales:
            adjusted.append(int(item))
            if len(adjusted) == len(weekly_tweets):
                break
        # print(len(weekly_sales), len(weekly_sentiment), len(weekly_tweets))

        weekly = pd.DataFrame({'dates': weekly_tweets.index,'tweet_count': weekly_tweets.values,
                              'sentiment': weekly_sentiment.values, 'sales': adjusted})
        weekly['movie'] = m_names[i]
        weekly.fillna(0, inplace=True)
        weekly_data = weekly_data.append(weekly, ignore_index=True)
        # print(weekly_data)
    return weekly_data

weekly_data = prepare_weekly()

# print(len(weekly_data))
weekly_data.to_csv('weeklt_data.csv', index=False)


