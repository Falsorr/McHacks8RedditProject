import praw
from string import punctuation
from stockInfo import stonks
app = praw.Reddit(client_id = 'FUzb37XqgvY_Kw', client_secret = 'mRsuht9Cb_LPJSQu9O_MwNEuB18cOw', \
                  user_agent = 'McHacks8RedditProject', username = 'IPissedMyBed404', password = 'HePissedTheBed404')
class redditSearcher():
    #app = praw.Reddit(client_id = 'FUzb37XqgvY_Kw', client_secret = 'mRsuht9Cb_LPJSQu9O_MwNEuB18cOw', \
    #              user_agent = 'McHacks8RedditProject', username = 'IPissedMyBed404', password = 'HePissedTheBed404')
    #subsOfInterest =[]
    #wordIndex ={}
    #codesOfInterest =[]
    #posts = []
    def __init__(self):
        self.app = app = praw.Reddit(client_id = 'FUzb37XqgvY_Kw', client_secret = 'mRsuht9Cb_LPJSQu9O_MwNEuB18cOw', \
                  user_agent = 'McHacks8RedditProject', username = 'IPissedMyBed404', password = 'HePissedTheBed404')
        self.subsOfInterest = []
        self.wordIndex = {}
        self.codesOfInterest = []
        self.posts = []
        self.stock = stonks()
        self.scale = 0
        print("initialized")
    def addSub(self,subName):
        self.subsOfInterest.append(subName)
    def addCode(self,code):
        codesOfInterest.append(code)
    def parse(self,areaOfInterest = "top",postLimit = 100):
        self.posts = []
        self.scale = postLimit
        for sub in self.subsOfInterest:
            if areaOfInterest == "top":
                self.posts.append(app.subreddit(sub).top(limit=postLimit))
            elif areaOfInterest == "new":
                self.posts.append(app.subreddit(sub).new(limit=postLimit))
            elif areaOfInterest == "hot":
                self.posts.append(app.subreddit(sub).new(limit=postLimit))
    def findPopularCodes(self):
        for subPosts in self.posts:
            for post in subPosts:
                for word in post.title.split():
                    word = word.translate(str.maketrans('','',punctuation))
                    if(len(word)<5):
                        word = word.upper()
                        #self.stock.addStock(word)
                        if word in self.wordIndex:
                            self.wordIndex[word]+=1
                        else:
                            self.wordIndex[word]=1
        for code in self.wordIndex:
            if self.wordIndex[code]>self.scale*0.1:
                self.stock.addStock(code)
        print("doneHere")
    def printCodes(self):
        codeData = self.stock.GetCodes()
        for word in codeData:
            print(word,codeData[word]['open'])
    def getCodes(self):
        return self.stock.GetCodes()


        




#test
#WSB = app.subreddit('Wallstreetbets')
#dict = {"$":5}
#desiredCodes = ["GME","AMC","NOK"]
#results = WSB.search("$GME",sort="new",time_filter="day")
#for t in results:
#    print(t.title)
