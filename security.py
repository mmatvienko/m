from iexfinance import Stock

class IEXSecurity:
    def __init__(self, ticker):
        self.ticker = ticker
        self.security = Stock(ticker)
        
    def get_price(self):
        return self.security.get_price()


class IEXTestSecurity:
    def __init__(self, ticker):
        self.ticker = ticker
        self.price = None        
        self.prices = None
        from iexfinance import get_historical_data
        from datetime import datetime
        start = datetime(2014, 1, 1)
        end = datetime(2018, 1, 1)
        df = get_historical_data(self.ticker, start=start, end=end, output_format='pandas')
        self.prices = df['open']
        print("Opening: ", self.prices[0])
        print("Closing: ", self.prices[-1])
        print("Days: ", len(self.prices))
        self.counter = 0

    def get_price(self):
        # do price grabbing stuff like talking to an API
        # self.price = time() % 32
        self.price = self.prices[self.counter]
        self.counter += 1
        return self.price # maybe append timestamp


class TestSecurity:
    def __init__(self, ticker):
        self.ticker = ticker
        self.price = None
        self.prices = None
        with open("data/goog_stock.csv", "r") as f:
            self.prices = [float(x.split(',')[3]) for x in f.readlines()[1:]]
        self.counter = 0

    def get_price(self):
        # do price grabbing stuff like talking to an API
        # self.price = time() % 32
        self.price = self.prices[self.counter]
        self.counter += 1
        return self.price # maybe append timestamp
