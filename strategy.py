from time import sleep
from utils import AutoQueue
from security import Security

class Strategy():
    def __init__(self):
        # TODO framework to test different parameter in parallel
        self.HZ = 5.0
        self.price_sum = 0
        # perhaps make arg in Q(arg) an arg in __init__
        self.prices = AutoQueue(10)
        self.price_sum_sq = 0
        self.count = 0
        self.boundary = 0.05    # percent change from mean

    # calculate average using a queue, be able to set size using some parameter
    def execute(self, portfolio):
        goog = Security("GOOG")
        counter = 0
        while counter < 750:
            price = goog.get_price()
            self.prices.put(price)

            # do things necessary for avg and stddev calc
            self.price_sum = self.prices.sum()
            self.price_sum_sq = self.prices.sum_sq()
            self.count = len(self.prices)

            avg = self.prices.average()
            var = self.prices.variance()
            
            if price < avg * (1 - self.boundary):
                # low price, want to buy
                while portfolio.buy(goog, 1): pass        
                self.holding = True
            elif price > avg * (1 + self.boundary):
                # high price, want to sell_all
                portfolio.sell_all(goog)
                self.holding = False
            print(f'Price: {price:.2f}\tAvg: {avg:.2f}\tvar: {var:.2f}')
            print(f'while counter: {counter}')
            counter += 1
            # sleep(1.0/self.HZ)
        print(portfolio)
