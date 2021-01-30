#Daniel Fassler
#Samer Sawan
#Mohammed ???

import praw
import tkinter as tk

HEIGHT = 800
WIDTH = 800

#Creating the app
app = praw.Reddit(client_id = 'FUzb37XqgvY_Kw', client_secret = 'mRsuht9Cb_LPJSQu9O_MwNEuB18cOw', \
                  user_agent = 'McHacks8RedditProject', username = 'IPissedMyBed404', password = 'HePissedTheBed404')

wsb = app.subreddit('Wallstreetbets')
hot_topics = wsb.hot(limit = 10)
for submission in hot_topics :
    print(submission.selftext, '\n\n\n')
    
    


#Creating the UI
root = tk.Tk()
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#The frame1 is used to get the user input, it has a label with instructions, an Entry for the input itself and a button to start searching
frame1 = tk.Frame(canvas, bg = 'gray')
frame1.place(relx = 0.1, rely = 0.05, relheight = 0.1, relwidth = 0.8, anchor ='nw')

instruction_fr1 = tk.Label(frame1, text = "Enter the stock code ($??) here: ")
instruction_fr1.place(rely = 0.1, relx = 0.01, relwidth = 0.4, relheight = 0.8, anchor = 'nw')

search_bar = tk.Entry(frame1)
search_bar.place(rely = 0.1, relx = 0.42, relwidth = 0.2, relheight = 0.8, anchor ='nw')

search_button = tk.Button(frame1, text = 'Search Reddit!')
search_button.place(rely = 0.1, relx = 0.67, relwidth = 0.3, relheight = 0.8, anchor = 'nw')

