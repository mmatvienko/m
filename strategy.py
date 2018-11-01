from time import sleep
from utils import AutoQueue
from security import IEXTestSecurity as TestSecurity
from security import IEXSecurity as Security

import time

class LiveTestStrat():
    """Same as Previous strat but this should use live prices
    and trade the same stratey as Strategy()
    """
    def __init__(self):
        self.HZ = 1.0/1.0
        self.local_strategies = [self.tsla]

        # variables needed for tsla()
        self.prices = AutoQueue(10)
        self.boundary = 0.01
        self.holding = False
        self.volume = 0
    def execute(self, portfolio):
        while True:
            for local_strategy in self.local_strategies:
                local_strategy()
            sleep(1.0/self.HZ)

    def tsla(self):
        tsla = Security('TSLA') 
        price = tsla.get_price()
        self.prices.put(price)
        volume = tsla.security.get_volume()
        # if volume != self.volume:
        #     print(volume)
        #     self.volume = volume
        # else:
        #     return

        # do things necessary for avg and stddev calc
        # self.price_sum = self.prices.sum()
        # self.price_sum_sq = self.prices.sum_sq()
        # self.count = len(self.prices)
        
        avg = self.prices.average()
        var = self.prices.variance()
    
        if price < avg * (1 - self.boundary):
            # low price, want to buy
            while portfolio.buy(tsla, 1): pass        
            self.holding = True
        elif price > avg * (1 + self.boundary):
            # high price, want to sell_all
            portfolio.sell_all(tsla)
            self.holding = False
        print(f'Price: {price:.2f}\tAvg: {avg:.2f}\tvar: {var:.2f} <{time.asctime()}', end='\r')
       

class Strategy():
    def __init__(self):
        # TODO framework to test different parameter in parallel
        self.HZ = 14000.0
        self.price_sum = 0
        # perhaps make arg in Q(arg) an arg in __init__
        self.prices = AutoQueue(10)
        self.price_sum_sq = 0
        self.count = 0
        self.boundary = 0.025    # percent change from mean

    # calculate average using a queue, be able to set size using some parameter
    def execute(self, portfolio):
        goog = TestSecurity("GOOG")
        counter = 0
        while counter < 949:
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
            # print(f'Price: {price:.2f}\tAvg: {avg:.2f}\tvar: {var:.2f}')
            counter += 1
            sleep(1.0/self.HZ)
        print(portfolio)
