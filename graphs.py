import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np


weekly_data = pd.read_csv('weeklt_data.csv')
total_sales = pd.read_csv('totally.csv')
ratings = pd.read_csv('ratings.csv')

m_names = ["ladyb", "thepost", "threebill", "shapeofwater", "phantom", "getout", "dunkirk", "darkest", "callme"]

threebill = weekly_data[weekly_data['movie']== 'threebill']
ladyb = weekly_data[weekly_data['movie']== 'ladyb']
thepost = weekly_data[weekly_data['movie']== 'thepost']
shapeofwater = weekly_data[weekly_data['movie']== 'shapeofwater']
phantom = weekly_data[weekly_data['movie']== 'phantom']
getout = weekly_data[weekly_data['movie']== 'getout']
dunkirk = weekly_data[weekly_data['movie']== 'dunkirk']
darkest = weekly_data[weekly_data['movie']== 'darkest']
callme = weekly_data[weekly_data['movie']== 'callme']

# labels=["4 Weeks Out", "3 Weeks Out", "2 Weeks Out", "1 Week Out", " Release Week",
#               "1 Week After", "2 Weeks After","3 Weeks After","4 Weeks After","5 Weeks After","6 Weeks After","7 Weeks After",
#               "8 Weeks After","9 Weeks After","10 Weeks After","11 Weeks After","12 Weeks After","13 Weeks After","14 Weeks After",
#                "15 Weeks After","16 Weeks After","17 Weeks After","18 Weeks After","19 Weeks After","20 Weeks After","21 Weeks After",
#                 "22 Weeks After","23 Weeks After","24 Weeks After","25 Weeks After","26 Weeks After","27 Weeks After",
#                 "28 Weeks After", "29 Weeks After"]
# plt.figure()
# plt.plot(np.arange(len(threebill)), threebill['sales'], linestyle= 'dashed')
# plt.plot(np.arange(len(ladyb)), ladyb['sales'], linestyle= 'dashed')
# plt.plot(np.arange(len(thepost)), thepost['sales'], linestyle= 'dashed')
# plt.plot(np.arange(len(shapeofwater)), shapeofwater['sales'], linestyle= 'dashed')
# plt.plot(np.arange(len(phantom)), phantom['sales'], linestyle= 'dashed')
# plt.plot(np.arange(len(getout)), getout['sales'], linestyle= 'dashed')
# plt.plot(np.arange(len(dunkirk)), dunkirk['sales'], linestyle= 'dashed')
# plt.plot(np.arange(len(darkest)), darkest['sales'], linestyle= 'dashed')
# plt.plot(np.arange(len(callme)), callme['sales'], linestyle= 'dashed')
# plt.legend(m_names, loc = 'best')
# plt.xticks(np.arange(len(dunkirk))-1.5, labels, rotation=45, size="medium" )
# plt.title('Box Office')



list_x = [callme['sentiment'].mean(), darkest['sentiment'].mean(), dunkirk['sentiment'].mean(), thepost['sentiment'].mean()
        , getout['sentiment'].mean(), threebill['sentiment'].mean(), shapeofwater['sentiment'].mean(),
         ladyb['sentiment'].mean(), phantom['sentiment'].mean()]
list_y = list(ratings['rating'])


# print(list_x)
# print(list_y)
fit = np.polyfit(list_x,list_y,1)
fit_fn = np.poly1d(fit)
# fit_fn is now a function which takes in x and returns an estimate for y

plt.plot(list_x,list_y, 'yo', list_x, fit_fn(list_x), '--k')
plt.title('Correlation between the sentiment and ratings')
plt.xlabel('sentiment scores')
plt.ylabel('rating scores')


# fig, ax1 = plt.subplots()
#
# ax1.bar(total_sales.index, total_sales['total_sales'], width = 0.6)
# ax1.set_title('Total Sales', fontsize = 14)
# ax1.tick_params('y', colors='b')
# ax1.set_xticks(ticks=total_sales.index-0.3)
# ax1.set_xticklabels((total_sales['movie']), rotation = 45)




# ax1.bar(three.index, three['sales'])
# ax1.set_title("Three Billboards Outside Ebbing, Missouri (Release Date: November 10, 2017)", fontsize = 16)
# ax1.set_xlabel('Weeks')
# ax1.set_ylabel('Weekly Sales', color='b')
# ax1.tick_params('y', colors='b')
# ax1.set_xticks(ticks=three.index-0.6)
# ax1.set_xticklabels(labels=( "4 Weeks Out", "3 Weeks Out", "2 Weeks Out", "1 Week Out", " Release Week",
#               "1 Week After", "2 Weeks After","3 Weeks After","4 Weeks After","5 Weeks After","6 Weeks After","7 Weeks After",
#               "8 Weeks After","9 Weeks After","10 Weeks After","11 Weeks After","12 Weeks After","13 Weeks After","14 Weeks After",
#                "15 Weeks After","16 Weeks After","17 Weeks After","18 Weeks After","19 Weeks After","20 Weeks After","21 Weeks After",
#                 "22 Weeks After","23 Weeks After","24 Weeks After","25 Weeks After","26 Weeks After","27 Weeks After",
#                 "28 Weeks After", "29 Weeks After"), rotation=45, size="medium" )
# ax2 = ax1.twinx()
# ax2.plot(three.index, three['tweet_count'],'k-')
# ax2.set_ylabel('Weekly Tweets', color='k')
# ax2.plot(ladyb_weekly.index, ladyb_weekly['sentiment'],'k-')
# ax2.set_ylabel('Weekly Sentiment', color='k')

plt.show()