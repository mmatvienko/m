import time
DEBUG = False
class Portfolio:
    def __init__(self, balance):
        self.balance = balance
        self.holdings = {}
        self.trades_made = 0

    def buy(self, security, quantity):
        if not self._can_purchase(security, quantity):
            return False
        # check if you can actully purchase
        purchase_price = security.price
        self.balance -= purchase_price * quantity
        if security in self.holdings:
            self.holdings[security] += quantity
        else:
            self.holdings[security] = quantity
        if DEBUG:
            print(f'purchased {quantity} shares of {security.ticker} at {purchase_price}')
            print(self.__str__())
        # maybe track the purchase in a serializable python class
        self.trades_made += 1
        return True


    def sell_all(self, security):
        if security in self.holdings:
            sale_price = security.price
            quantity = self.holdings[security]
            self.balance += sale_price * quantity
            del self.holdings[security]
            self.trades_made += 1
            if DEBUG:
                print(f'sold {quantity}x{security.ticker} for {sale_price*quantity}')
                print(f'balance is now {self.balance}')
            return True
        return False


    def _can_purchase(self, security, quantity):
        # define this based on whatever metric
        return self.balance > security.price * quantity

    def __str__(self):
        total_equity = sum([security.price * self.holdings[security] for security in self.holdings])
        return f'Cash: {self.balance:.2f}\tEquity: {total_equity}\tTotal: {(total_equity + self.balance):.2f}\tTrades made: {self.trades_made}'
