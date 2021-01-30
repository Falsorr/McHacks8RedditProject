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


#The subbredits used 
WSB = app.subreddit('Wallstreetbets')
SMS = app.subreddit('smallstreetbets')
STK = app.subreddit('stocks')
INV = app.subreddit('investing')

ALL_SUBS = (WSB, SMS, STK, INV)


def search_reddit(stock_code, type_of_search):
    """The search function : depending on the type_of_search it will do a search related to the code provided,
    then order by upvotes if type_of_search is 'top', order by date if type_of_search is 'new' or order by comments if type_of_search is 'hot'
    """

    results = ""
    relevant_post = []
    total_post = []
    
    if type_of_search == 'top' :
        for sub in ALL_SUBS:
            submissions = sub.top(limit=50)
            for post in submissions:
                if stock_code.upper() in post.title:
                    results += f'Upvotes: {post.score}\t{post.url}\n'
                    relevant_post.append(post)
                total_post.append(post)
    
    elif type_of_search == 'new' :
        for sub in ALL_SUBS:
            submissions = sub.new(limit=50)
            for post in submissions:
                if stock_code.upper() in post.title:
                    results += f'Upvotes: {post.score}\t{post.url}\n'
                    relevant_post.append(post)
                total_post.append(post)
    
    
    else :
        for sub in ALL_SUBS:
            submissions = sub.hot(limit=50)
            for post in submissions:
                if stock_code.upper() in post.title:
                    results += f'Upvotes: {post.score}\t{post.url}\n'
                    relevant_post.append(post)
                total_post.append(post)

    related_posts = f'There are {len(relevant_post)} posts about ${stock_code.upper()} out of the {len(total_post)} found \n\n'
    display_label.configure(text = related_posts + results)
        





#Creating the UI
root = tk.Tk()
root.title('Search Reddit Program')
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#The frame1 is used to get the user input, it has a label with instructions, an Entry for the input itself and buttons to start searching
frame1 = tk.Frame(canvas, bg = '#CEE3F8', )
frame1.place(relx = 0.05, rely = 0.05, relheight = 0.2, relwidth = 0.9, anchor ='nw')

instruction_fr1 = tk.Label(frame1, text = "Enter the stock code here: ")
instruction_fr1.place(rely = 0.1, relx = 0.20, relwidth = 0.4, relheight = 0.3, anchor = 'nw')

search_bar = tk.Entry(frame1)
search_bar.place(rely = 0.1, relx = 0.60, relwidth = 0.2, relheight = 0.3, anchor ='nw')

#Search by the most popular result
top_button = tk.Button(frame1, text = 'Search by top', command = lambda: search_reddit(search_bar.get(), 'top'))
top_button.place(rely = 0.41, relx = 0.18, relwidth = 0.2, relheight = 0.25, anchor = 'nw')

#Search by the newest result
new_button = tk.Button(frame1, text = 'Search by new', command = lambda: search_reddit(search_bar.get(), 'new'))
new_button.place(rely = 0.41, relx = 0.40, relwidth = 0.2, relheight = 0.25, anchor = 'nw')

#Search by results with most comments
hot_button = tk.Button(frame1, text = 'Search by hot', command = lambda: search_reddit(search_bar.get(), 'hot'))
hot_button.place(rely = 0.41, relx = 0.62, relwidth = 0.2, relheight = 0.25, anchor = 'nw')

#Display frame : The frame where all the info is displayed, it is basically a giant label to write on it
display_frame = tk.Frame(canvas, bg = '#FF4500')
display_frame.place(relx = 0.05, rely = 0.3, relwidth = 0.9, relheight = 0.6, anchor = 'nw')

display_label = tk.Label(display_frame, text = "Empty at the moment, start searching Reddit!", anchor = 'nw', justify = 'left')
display_label.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.98, anchor = 'nw')

root.mainloop()
