#Daniel Fassler
#Samer Sawan
#Mohammed ???

import praw

#Creating the app
app = praw.Reddit(client_id = 'FUzb37XqgvY_Kw', client_secret = 'mRsuht9Cb_LPJSQu9O_MwNEuB18cOw', \
                  user_agent = 'McHacks8RedditProject', username = 'IPissedMyBed404', password = 'HePissedTheBed404')

wsb = app.subreddit('Wallstreetbets')
