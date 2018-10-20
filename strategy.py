from time import sleep
from utils import AutoQueue
from security import Security

class Strategy():
    def __init__(self):
        self.HZ = 5.0
        self.price_sum = 0
        # perhaps make arg in Q(arg) an arg in __init__
        self.prices = AutoQueue(20)
        self.price_sum_sq = 0
        self.count = 0

    # calculate average using a queue, be able to set size using some parameter
    def execute(self, portfolio):
        goog = Security("GOOG")
        while True:
            price = goog.get_price()

            # make space in queue if necessary
            self.prices.put(price)
            # do things necessary for avg and stddev calc
            # perhaps make these calculations more efficient?
            # is O(1) tho as long as AutoQueue.size doesn't scale
            self.price_sum = self.prices.sum()
            self.price_sum_sq = self.prices.sum_sq()
            self.count = len(self.prices)

            # if goog.get_price() < 6:
            #     portfolio.buy(goog, 3)
            # if goog.get_price() > 27:
            #     portfolio.sell_all(goog)
            avg = self.price_sum / self.count
            var = (self.price_sum_sq - ((self.price_sum)**2)/self.count) / self.count
            print(f'Price: {price:.2f}\tAvg: {avg:.2f}\tvar: {var:.2f}')
            sleep(1.0/self.HZ)
