# This file should hopefully run everything... probably good if I design everything first
from portfolio import Portfolio
from queue import Queue
from threading import Thread

import strategy, time, sys

"""
hopefully can read all strategies in a module print them out for user to choose.
UPDATE: nice, it works. use this to display strategies.
most likely portoflios will be serialized and encrypted (if possible) 
and perhaps along with account
"""

import inspect
print([m[0] for m in inspect.getmembers(strategy, inspect.isclass) if m[1].__module__ == 'strategy'])

sys.exit()

def worker():
    """Simple worker daemon to execute trading jobs"""
    while True:
        strat, portfolio = jobs.get()
        strat.execute(portfolio)
        jobs.task_done()

jobs = Queue()

for i in range(3):
    t = Thread(target=worker)
    t.daemon = True
    t.start()



# THIS IS NOT THREAD SAFE AT ALL
"""
Using multiple strats 'looks better' than using a single one. 
Makes sense since Strategy stores state. Strategy should really just dictate how everything runs
"""
strat = strategy.Strategy()
strat1 = strategy.Strategy()
strat2 = strategy.Strategy()
port1 = Portfolio(1000)
port2 = Portfolio(2000)
port3 = Portfolio(3000)
jobs.put((strat, port1))
jobs.put((strat1, port2))
jobs.put((strat2, port3))

jobs.join()



# have a thing that handles a queue of order and this object can only run when markets are open.
# so queue fills when markets closed
"""portfolio = Portfolio(1000)
strategy = strategy.Strategy()"""

# spawn a thread to run strategy
"""strategy.execute(portfolio)"""
