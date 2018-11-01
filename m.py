# This file should hopefully run everything... probably good if I design everything first
from portfolio import Portfolio
from queue import Queue
from threading import Thread

import strategy, time, sys
import inspect

print("Strategies\n")

strategies = [m for m in inspect.getmembers(strategy, inspect.isclass) if m[1].__module__ == 'strategy']
for i, strategy in enumerate(strategies):
    print(f'[{i + 1}] {strategy[0]}')

print('\nSelection: ', end='' )
strat_num = int(input()) - 1
strat = strategies[strat_num][1]()


def worker():
    """Simple worker daemon to execute trading jobs"""
    while True:
        strat, portfolio = jobs.get()
        strat.execute(portfolio)
        jobs.task_done()

jobs = Queue()

for i in range(1):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

# THIS IS NOT THREAD SAFE AT ALL
"""
Using multiple strats 'looks better' than using a single one. 
Makes sense since Strategy stores state. Strategy should really just dictate how everything runs
"""

port = Portfolio(10000)
jobs.put((strat, port))
jobs.join()



# have a thing that handles a queue of order and this object can only run when markets are open.
# so queue fills when markets closed
"""portfolio = Portfolio(1000)
strategy = strategy.Strategy()"""

# spawn a thread to run strategy
"""strategy.execute(portfolio)"""
