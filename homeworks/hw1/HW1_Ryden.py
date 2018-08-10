import numpy
import datetime

class Portfolio(object):
    def __init__(self, cash = 0):
        self.cash = float(cash)
        self.stock = 'None'
        self.mf = 'None'
        self.bond = 'None'
        self.transactions = []
    
    def __str__(self):
        return """
    As of %s
    -----------------------
    Cash:    %.2f
    Stock:   %s
    M.funds: %s
    Bonds:   %s
        """ % (self.stampTime(), self.cash, self.sortInvestments(self.stock), self.sortInvestments(self.mf), self.sortInvestments(self.bond))
    
    def sortInvestments(self, investment):
        if investment == 'None':
            return investment
        else:
            show_investment = sorted(['%s --- %.2f shares' % (i, investment[i]) for i in investment])
            return '\n\t     '.join(show_investment)
    
    def __repr__(self):
        return self.__str__()
    
    def stampTime(self):
        return datetime.datetime.now().strftime("%I:%M%p on %m/%d/%Y")
        
    def addCash(self, amount, is_add = True):
        self.cash += float(amount)
        if is_add:
            self.transactions.append('%s | Added cash: $%.2f' % (self.stampTime(), amount))
        
    def withdrawCash(self, amount, is_cash = True, shares = 0, investment = Stock(1, 'Empty')):
        if amount > self.cash:
            line1 = 'Insufficient funds.'
        else:
            self.addCash(-amount, is_add = False)
            if is_cash:
                line1 = 'Withdrew $%.2f from your portfolio.' % (amount)
                self.transactions.append('%s | Withdrew cash: $%.2f' % (self.stampTime(), amount))
            else: 
                line1 = 'You bought %.2f shares of %s for $%.2f.' % (shares, investment.ticker, amount)
                self.transactions.append('%s | Bought shares: %.2f (%s) @ $%.2f/s ($%.2f total)' % (self.stampTime(), shares, investment.ticker, investment.price, amount))
        print """
    %s
    You have $%.2f remaining in your portfolio.
        """ % (line1, self.cash)
        
    def buyInvestment(self, shares, investment, my_shares):
        cost = shares * investment.price
        self.withdrawCash(cost, False, shares, investment)
        if my_shares == 'None':
            my_shares = {investment.ticker : shares}
        elif investment.ticker in my_shares.keys():
            my_shares[investment.ticker] += shares
        else:
            my_shares[investment.ticker] = shares
        return my_shares
        
    def buyStock(self, shares, investment):
        self.stock = self.buyInvestment(shares, investment, self.stock)
    
    def buyMutualFund(self, shares, investment):
        self.mf = self.buyInvestment(shares, investment, self.mf)
    
    def buyBond(self, shares, investment):
        self.bond = self.buyInvestment(shares, investment, self.bond)
     
    def sellInvestment(self, shares, investment, my_shares, sale_price):
        if investment.ticker not in my_shares:
            print 'You do not own any shares of that investment.'
            return my_shares
        elif shares > my_shares[investment.ticker]:
            print """
    Cannot sell %.2f shares of %s. 
    You only own %.2f shares.
            """ % (shares, investment.ticker, my_shares[investment.ticker])
            return my_shares
        else:
            earnings = sale_price * investment.price * shares
            profit = earnings - (shares * investment.price)
            self.cash += earnings
            if shares == my_shares[investment.ticker]:
                del my_shares[investment.ticker]
            else:
                my_shares[investment.ticker] -= shares
            print """
    Sold %.2f shares of %s at $%.2f per share.
    You have %.2f shares remaining.
    The sale was worth $%.2f, for a profit of $%.2f.
    You now have $%.2f in your portfolio.
            """ % (shares, investment.ticker, sale_price * investment.price, my_shares[investment.ticker], earnings, profit, self.cash)
            self.transactions.append('%s | Sold shares: %.2f (%s) for $%.2f/s ($%.2f total)' % (self.stampTime(), shares, investment.ticker, sale_price * investment.price, sale_price * investment.price * shares))
            investment.price = sale_price
            return my_shares
    
    def sellStock(self, shares, investment):
        self.stock = self.sellInvestment(shares, investment, self.stock, numpy.random.uniform(0.5, 1.5))

    def sellMutualFund(self, shares, investment):
        self.mf = self.sellInvestment(shares, investment, self.mf, numpy.random.uniform(0.9, 1.2))

    def sellBond(self, shares, investment):
        self.bond = self.sellInvestment(shares, investment, self.bond, 1.02)
    
    def history(self, from_start = True):
        if from_start:
            print '\n'.join(self.transactions)
        else:
            print '\n'.join(reversed(self.transactions))
    
    
    
    
class Investment(object):
    def __init__(self, price, ticker):
        self.ticker = str(ticker)
        self.price = float(price)
    
    def __str__(self):
        return '%s: $%.2f per share' % (self.ticker, self.price)
    
    def __repr__(self):
        return self.__str__()
    
class Stock(Investment):
    def __init__(self, price, ticker):
        if isinstance(price, float):
            print """
    Stock prices must be integer values.
    Input rounded down to $%d.
            """% (int(price))
        Investment.__init__(self, int(price), ticker)
        
class MutualFund(Investment):
    def __init__(self, ticker, price = 1):
        Investment.__init__(self, 1, ticker)

class Bond(Investment):
    def __init__(self, price, ticker):
        Investment.__init__(self, price, ticker)