import yfinance as yf
from get_all_tickers import get_tickers as gt
class stonks():
    
    def __init__(self):
        self.stockData = {}
    def addStock(self,ticker):
        if ticker in self.stockData:
            return
        try:
            self.stockData[ticker] = yf.Ticker(ticker).info
        except: 
            return
    def GetCodes(self):
        return self.stockData
