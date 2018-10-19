from time import time, sleep

class Strategy():
    def __init__(self):
        self.HZ = 5.0
        self.price_sum = 0
        self.price_sum_sq = 0
        self.count = 0

    # calculate average using a queue, be able to set size using some parameter
    def execute(self, portfolio):
        goog = Security("GOOG")
        while True:
            price = goog.get_price()

            # do things necessary for avg and stddev calc
            self.price_sum += price
            self.price_sum_sq += price**2
            self.count += 1.0

            # if goog.get_price() < 6:
            #     portfolio.buy(goog, 3)
            # if goog.get_price() > 27:
            #     portfolio.sell_all(goog)
            avg = self.price_sum / self.count
            var = (self.price_sum_sq - ((self.price_sum)**2)/self.count) / self.count
            print(f'Price: {price:.2f}\tAvg: {avg:.2f}\tvar: {var:.2f}')
            sleep(1.0/self.HZ)


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


class Portfolio:
    def __init__(self, balance):
        self.balance = balance
        self.holdings = {}

    def buy(self, security, quantity):
        if not self.can_purchase(security, quantity):
            return False
        # check if you can actully purchase
        purchase_price = security.get_price()
        self.balance -= purchase_price * quantity
        if security in self.holdings:
            self.holdings[security] += quantity
        else:
            self.holdings[security] = quantity
        print(f'purchased {quantity} shares of {security.ticker} at {purchase_price}')
        print(f'balance is now {self.balance}')
        # maybe track the purchase in a serializable python class
        return True


    def sell_all(self, security):
        if security in self.holdings:
            sale_price = security.get_price()
            quantity = self.holdings[security]
            self.balance += sale_price * quantity
            del self.holdings[security]
            print(f'sold {quantity}x{security.ticker} for {sale_price*quantity}')
            print(f'balance is now {self.balance}')

            return True
        return False
    

    def can_purchase(self, security, quantity):
        # define this based on whatever metric
        return self.balance > security.get_price() * quantity
