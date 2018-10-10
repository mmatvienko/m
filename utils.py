from time import time

class Security:
    def __init__(self, ticker):
        self.ticker = ticker
        self.price = None


    def get_price(self):
        # do price grabbing stuff like talking to an API
        self.price = time() % 32
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
