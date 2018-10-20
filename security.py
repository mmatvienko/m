class Security:
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
