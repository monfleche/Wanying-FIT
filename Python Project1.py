################################################################################################
##
##  Python Project
##  Master 2 FIT
##  Wanying ZHAO & Amadou DJIBO
##
#################################################################################################


# import packages

import pandas as pd
import numpy as np
import os
import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from random import randint

##############Create Bonds#############

class Bonds(object):
    def __init__(self, minimum_term, minimum_amount, yearly_interest_rate):
        self.minimum_term = minimum_term
        self.minimum_amount = minimum_amount
        self.yearly_interest_rate = yearly_interest_rate

    def CalculateInvestment(self, period):
        investment = self.minimum_amount * ((1 + self.yearly_interest_rate) ** period)
        return investment


Short_term_bonds = Bonds(2, 1000, 0.01)
Long_term_bonds = Bonds(5, 3000, 0.05)

period = []
Short_term_investment = []
Long_term_investment = []

for t in range(101):
    period.append(t)
    Short_term_investment.append(Short_term_bonds.CalculateInvestment(t))
    Long_term_investment.append(Long_term_bonds.CalculateInvestment(t))
#print([period, Short_term_investment, Long_term_investment])

################## PLOT ###################
# optional style
# matplotlib.style.use('ggplot')#

# plt.plot(period, Short_term_investment)
# plt.plot(period, Long_term_investment)
# plt.legend(['Short term', 'Long term'], loc='upper left')
# plt.xlabel('Period')
# plt.ylabel('Investment')
# plt.title('Investment Evolution')
# plt.grid(True)
# plt.savefig(os.path.abspath('./BondsRevolution.png'))
# plt.show()


################################################################################################################################

##############Create Stocks#############

Stock_AAPL = pd.read_csv('.\Data\AAPL.csv', sep=';',parse_dates=['Date'])
Stock_AXP = pd.read_csv('.\Data\AXP.csv', sep=';',parse_dates=['Date'])
Stock_FDX = pd.read_csv('.\Data\FDX.csv', sep=';',parse_dates=['Date'])
Stock_GOOGL = pd.read_csv('.\Data\GOOGL.csv', sep=';',parse_dates=['Date'])
Stock_IBM = pd.read_csv('.\Data\IBM.csv', sep=';',parse_dates=['Date'])
Stock_KO = pd.read_csv('.\Data\KO.csv', sep=';',parse_dates=['Date'])
Stock_MS = pd.read_csv('.\Data\MS.csv', sep=';',parse_dates=['Date'])
Stock_NOK = pd.read_csv('.\Data\K.csv', sep=';',parse_dates=['Date'])#Import issue, change de file name manually
Stock_XOM = pd.read_csv('.\Data\XOM.csv', sep=';',parse_dates=['Date'])
Stock_YHOO = pd.read_csv('.\Data\YHOO.csv', sep=';',parse_dates=['Date'])
#print(Stock_GOOGL)


#print(Stock_AAPL)
STOCK=[Stock_AAPL,Stock_AXP, Stock_FDX, Stock_GOOGL, Stock_IBM, Stock_KO, Stock_MS, Stock_NOK, Stock_XOM, Stock_YHOO]
#print(STOCK[0])

#write a function to calculate stock returns
def stock_return(stock, startday, endday):
    startday = pd.Timestamp(startday).date()
    endday = pd.Timestamp(endday).date()
    while not (Stock_AAPL['Date']==startday).any():
        startday = startday + datetime.timedelta(days=1)
    while not (Stock_AAPL['Date']==endday).any():
        endday=endday + datetime.timedelta(days=1)
    buyprice=float(stock[(stock['Date']==startday)]['High'])
    sellprice=float(stock[(stock['Date']==endday)]['High'])
    return (sellprice-buyprice)/buyprice

#print(stock_return(Stock_AAPL.dataframe, '20050103', '20050108'))



################## PLOT ###################
matplotlib.style.use('ggplot')

plt.plot(Stock_AAPL['Date'], Stock_AAPL['High'])
plt.plot(Stock_AXP['Date'], Stock_AXP['High'])
plt.plot(Stock_FDX['Date'], Stock_FDX['High'])
plt.plot(Stock_GOOGL['Date'], Stock_GOOGL['High'])
plt.plot(Stock_IBM['Date'], Stock_IBM['High'])
plt.plot(Stock_KO['Date'], Stock_KO['High'])
plt.plot(Stock_MS['Date'], Stock_MS['High'])
plt.plot(Stock_NOK['Date'], Stock_NOK['High'])
plt.plot(Stock_XOM['Date'], Stock_XOM['High'])
plt.plot(Stock_YHOO['Date'], Stock_YHOO['High'])

plt.legend(['AAPL', 'AXP', 'FDX', 'GOOGL', 'IBM', 'KO', 'MS', 'NOK', 'XOM', 'YHOO'], loc='upper left')

plt.xlabel('Period')
plt.ylabel('StockPrice')
plt.title('Stock Price Evolution')
plt.grid(True)
plt.savefig(os.path.abspath('./Stock.png'))
plt.show()

#############################################################################################################################################################
############Creat Investor########################
class Investment(object):
    def __init__(self, stock, amount):
        self.stock=stock
        self.amount=amount

class ListInvestor(object):
    def __init__(self, budget, mode):
        self.budget = budget
        self.mode = mode

    def defensive_Investement(self, period):
        short_term = self.budget * float(randint(1, 10) / 10)
        long_term = self.budget - short_term
        if long_term % 2000 != 0:
            short_term = short_term + 1000
            long_term = long_term - 1000
        return short_term * (1 + Short_term_bonds.yearly_interest_rate) ** period + long_term * (1 + Long_term_bonds.yearly_interest_rate) ** period

    def aggressive_Investment(self, startday, endday):
        Investment=[]
        start= pd.Timestamp(startday).date()
        end= pd.Timestamp(endday).date()
        while not (Stock_AAPL['Date'] == start).any():
            start = start + datetime.timedelta(days=1)
        while not (Stock_AAPL['Date'] ==end).any():
            end = end + datetime.timedelta(days=1)
        while self.budget>100:
            rnd=randint(0,9)
            print(rnd)
            price = float(STOCK[rnd][(STOCK[rnd]['Date'] == start)]['High'])
            volume=randint(1,int(self.budget/price/2+1))
            Investment.append([rnd,volume*price, stock_return(STOCK[rnd],startday,endday)])
            self.budget=self.budget-volume*price
            print(self.budget)
        Investment = pd.DataFrame(Investment)
        print("first part finished")
        # df = df.transpose()
        Investment.columns = ['Stock', 'Amount', 'Return']
        return Investment


Defensive = ListInvestor(12000, 'defensive')
Aggressive = ListInvestor(12000, 'aggressive')

print(Aggressive.aggressive_Investment('20050103','20050108'))
