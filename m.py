# This file should hopefully run everything... probably good if I design everything first
from accounts import AlphaVantage
from utils import Security, Portfolio
import time

apikey = AlphaVantage.apiKey


# have a thing that handles a queue of order and this object can only run when markets are open.
# so queue fills when markets closed
goog = Security("GOOG")
portfolio = Portfolio(1000)
while True:
    print(goog.get_price())
    if goog.get_price() < 6:
        portfolio.buy(goog, 3)
    if goog.get_price() > 27:
        portfolio.sell_all(goog)
    time.sleep(1)
