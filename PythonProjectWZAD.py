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
import dis
import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from random import randint
from datetime import date



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
#optional style
matplotlib.style.use('ggplot')#

plt.plot(period, Short_term_investment)
 plt.plot(period, Long_term_investment)
 plt.legend(['Short term', 'Long term'], loc='upper left')
 plt.xlabel('Period')
 plt.ylabel('Investment')
 plt.title('Investment Evolution')
 plt.grid(True)
 plt.savefig(os.path.abspath('./BondsRevolution.png'))
 plt.show()


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

#print(stock_return(Stock_AAPL, '20050103', '20050108'))



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

class ListInvestor(object):
    def __init__(self, budget, type,start):
        self.budget = budget
        self.type = type
        self.start=start

class Defensive(ListInvestor):

    def defensive_Investement(self, startday, endday):
        self.budget = self.start
        start = pd.Timestamp(startday).date()
        end = pd.Timestamp(endday).date()
        if (end-start).days/360>Long_term_bonds.minimum_term:
            short_term = self.budget * float(randint(1, 10) / 10)
            long_term = self.budget - short_term
            if long_term % 2000 != 0:
                short_term = short_term + 1000
                long_term = long_term - 1000
            return short_term * ((1 + Short_term_bonds.yearly_interest_rate) ** ((end-start).days/360)) + long_term * ((1 + Long_term_bonds.yearly_interest_rate) ** ((end-start).days/360))
        elif (end-start).days/360 > Short_term_bonds.minimum_term:
            short_term=self.budget
            return short_term * ((1 + Short_term_bonds.yearly_interest_rate) ** ((end-start).days/360))
        else :
            return 0

# Create a list of 1000 defensive investors
DefensiveInvestor = dict()
for i in range(1, 1001):
    DefensiveInvestor[i] = Defensive(12000, 'Defensive',12000)
#print(DefensiveInvestor[1000].budget)





#Class name Aggressive
class Aggressive(ListInvestor):
    def aggressive_Investment(self, startday, endday):
        self.budget = self.start
        Investment=[]
        start= pd.Timestamp(startday).date()
        end= pd.Timestamp(endday).date()
        while not (Stock_AAPL['Date'] == start).any():
            start = start + datetime.timedelta(days=1)
        while not (Stock_AAPL['Date'] ==end).any():
            end = end + datetime.timedelta(days=1)
        while self.budget>100:
            rnd=randint(0,9)
            buyprice = float(STOCK[rnd][(STOCK[rnd]['Date'] == start)]['High'])
            sellprice= float(STOCK[rnd][(STOCK[rnd]['Date'] == end)]['High'])
            volume=randint(1,(int(self.budget/buyprice/2)+1))
            Investment.append(volume*sellprice)
            self.budget=self.budget-volume*buyprice
        return sum(Investment)

#Create a list of 1000 aggressive investors
AggressiveInvestor = dict()
for i in range(1, 1001):
    AggressiveInvestor[i] = Aggressive(12000, 'Aggressive',12000)
#print(AggressiveInvestor[1000].budget)
#print( AggressiveInvestor[1].aggressive_Investment('20050101','20060101'))



class Mixed(ListInvestor):
    def mixed_Investment(self, startday, endday):
        self.budget = self.start
        Investment=[]
        start = pd.Timestamp(startday).date()
        end = pd.Timestamp(endday).date()
        while self.budget>Short_term_bonds.minimum_amount:
            if (end-start).days/360>Long_term_bonds.minimum_term:
                    rnd=randint(0,1)
                    if rnd==0:
                        rnd=randint(0,1)
                        if rnd==0:
                         Investment.append(Short_term_bonds.minimum_amount * ((1 + Short_term_bonds.yearly_interest_rate) ** ((end - start).days/365)))
                         self.budget = self.budget- Short_term_bonds.minimum_amount
                        else:
                         Investment.append(Long_term_bonds.minimum_amount * ((1 + Long_term_bonds.yearly_interest_rate) ** ((end - start).days / 365)))
                         self.budget = self.budget- Long_term_bonds.minimum_amount
                    else:
                        while not (Stock_AAPL['Date'] == start).any():
                            start = start + datetime.timedelta(days=1)
                        while not (Stock_AAPL['Date'] == end).any():
                            end = end + datetime.timedelta(days=1)
                        rnd = randint(0, 9)
                        buyprice = float(STOCK[rnd][(STOCK[rnd]['Date'] == start)]['High'])
                        sellprice=float(STOCK[rnd][(STOCK[rnd]['Date'] == end)]['High'])
                        volume = randint(1, int(self.budget / buyprice / 2 + 1))
                        Investment.append(volume*sellprice)
                        self.budget = self.budget- volume * buyprice
            elif (end-start).days/360 > Short_term_bonds.minimum_term:
                rnd = randint(0, 1)
                if rnd == 0:
                    Investment.append(Short_term_bonds.minimum_amount * ((1 + Short_term_bonds.yearly_interest_rate) ** ((end - start).days / 360)))
                    self.budget = self.budget - Short_term_bonds.minimum_amount
                else:
                    while not (Stock_AAPL['Date'] == start).any():
                        start = start + datetime.timedelta(days=1)
                    while not (Stock_AAPL['Date'] == end).any():
                        end = end + datetime.timedelta(days=1)
                    rnd = randint(0, 9)
                    buyprice = float(STOCK[rnd][(STOCK[rnd]['Date'] == start)]['High'])
                    sellprice = float(STOCK[rnd][(STOCK[rnd]['Date'] == end)]['High'])
                    volume = randint(1, int(self.budget / buyprice / 2 + 1))
                    Investment.append(volume*sellprice)
                    self.budget = self.budget - volume * buyprice
            else:
                while not (Stock_AAPL['Date'] == start).any():
                    start = start + datetime.timedelta(days=1)
                while not (Stock_AAPL['Date'] == end).any():
                    end = end + datetime.timedelta(days=1)
                rnd = randint(0, 9)
                buyprice = float(STOCK[rnd][(STOCK[rnd]['Date'] == start)]['High'])
                sellprice = float(STOCK[rnd][(STOCK[rnd]['Date'] == end)]['High'])
                volume = randint(1, int(self.budget / buyprice / 2 ))
                Investment.append(volume*sellprice)
                self.budget = self.budget - volume * buyprice
        return sum(Investment)

MixedInvestor = dict()
for i in range(1, 1001):
    MixedInvestor[i] = Mixed(12000, 'Mixed', 12000)
#print(DefensiveInvestor[1000].budget)
#print(MixedInvestor[1000].mixed_Investment('20050103','20150108'))

#############################################################################################################################################################################
#############################################################################################################################################################################
