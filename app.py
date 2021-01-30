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
    

#Creating the UI
root = tk.Tk()
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#The frame1 is used to get the user input, it has a label with instructions, an Entry for the input itself and buttons to start searching
frame1 = tk.Frame(canvas, bg = '#CEE3F8')
frame1.place(relx = 0.05, rely = 0.05, relheight = 0.2, relwidth = 0.9, anchor ='nw')

instruction_fr1 = tk.Label(frame1, text = "Enter the stock code ($??) here: ")
instruction_fr1.place(rely = 0.1, relx = 0.20, relwidth = 0.4, relheight = 0.3, anchor = 'nw')

search_bar = tk.Entry(frame1)
search_bar.place(rely = 0.1, relx = 0.60, relwidth = 0.2, relheight = 0.3, anchor ='nw')

#Search by the most popular result
top_button = tk.Button(frame1, text = 'Search by top')
top_button.place(rely = 0.41, relx = 0.18, relwidth = 0.2, relheight = 0.25, anchor = 'nw')

#Search by the newest result
new_button = tk.Button(frame1, text = 'Search by new')
new_button.place(rely = 0.41, relx = 0.40, relwidth = 0.2, relheight = 0.25, anchor = 'nw')

#Search by results with most comments
hot_button = tk.Button(frame1, text = 'Search by hot')
hot_button.place(rely = 0.41, relx = 0.62, relwidth = 0.2, relheight = 0.25, anchor = 'nw')





#Display frame : The frame where all the info is displayed, it is basically a giant label to write on it
display_frame = tk.Frame(canvas, bg = '#FF4500')
display_frame.place(relx = 0.05, rely = 0.3, relwidth = 0.9, relheight = 0.6, anchor = 'nw')

display_label = tk.Label(display_frame, text = "Empty at the moment, start searching Reddit!")
display_label.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.98, anchor = 'nw')
