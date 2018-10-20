from time import time, sleep
from queue import Queue
DEBUG = False

class AutoQueue():              # For fun implement this in C++ and call from python?
    """A queue that can automatically throws out elements if full.
    Can also print contents of the queue
    """
    
    def __init__(self, max_size=5):
        self.contents = []
        self.MAX_SIZE = max_size
        self.filled = False     # not really true if max_size=0

    def put(self, item):
        # TODO method is super ugly, fix
        # check on fill
        if not self.filled:
            self.contents.append(item)
            if self.MAX_SIZE == len(self.contents):
                self.filled = True
        else:
            del self.contents[0]
            self.contents.append(item)

    def sum(self):
        return sum(self.contents)

    def sum_sq(self):
        return sum([x**2 for x in self.contents])

    def average(self):
        return self.sum()/self.length()

    def variance(self):
        return (self.sum_sq() - (self.sum()**2)/self.length()) / self.length()
    
    def __str__(self):
        return str(self.contents)

    def __len__(self):
        # TODO can just store length and save even more compute time
        if self.filled:
            if DEBUG:
                print('quick length')
            return self.MAX_SIZE
        if DEBUG:
            print('calculated length')
        return len(self.contents)
