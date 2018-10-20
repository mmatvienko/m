# This file should hopefully run everything... probably good if I design everything first
from accounts import AlphaVantage
from strategy import Strategy
from portfolio import Portfolio

apikey = AlphaVantage.apiKey


# have a thing that handles a queue of order and this object can only run when markets are open.
# so queue fills when markets closed
portfolio = Portfolio(1000)
strategy = Strategy()

# spawn a thread to run strategy
strategy.execute(portfolio)
