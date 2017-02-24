################################################################################################
##
##  Python Project
##  Master 2 FIT
##  Wanying ZHAO & Amadou DJIBO
##
#################################################################################################


# import packages

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
import os



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
print([period, Short_term_investment, Long_term_investment])

# optional style
# matplotlib.style.use('ggplot')

# plt.plot(period, Short_term_investment)
# plt.plot(period, Long_term_investment)
# plt.legend(['Short term', 'Long term'], loc='upper left')
# plt.xlabel('Period')
# plt.ylabel('Investment')
# plt.title('Investment Evolution')
# plt.grid(True)
# plt.savefig(os.path.abspath('./BondsRevolution.png'))
# plt.show()

##############Create Stocks#############

Stock_AAPL = pd.read_csv('.\Data\AAPL.csv', sep=';')
#print(Stock_AAPL)
Stock_AXP = pd.read_csv('.\Data\AXP.csv', sep=';')
Stock_FDX = pd.read_csv('.\Data\FDX.csv', sep=';')
Stock_GOOGL = pd.read_csv('.\Data\GOOGL.csv', sep=';')
Stock_IBM = pd.read_csv('.\Data\IBM.csv', sep=';')
Stock_KO = pd.read_csv('.\Data\KO.csv', sep=';') #Import issue, change de file name manually
Stock_MS = pd.read_csv('.\Data\MS.csv', sep=';')
Stock_NOK = pd.read_csv('.\Data\K.csv', sep=';')
Stock_XOM = pd.read_csv('.\Data\XOM.csv', sep=';')
Stock_YHOO = pd.read_csv('.\Data\YHOO.csv', sep=';')

#keep only date and high columns
AAPL  = Stock_AAPL[['Date','High']]
AAPL.rename(columns={'High': 'AAPL'}, inplace=True)
print(AAPL.head())
AXP  = Stock_AXP[['Date','High']]
AXP.rename(columns={'High': 'AXP'}, inplace=True)
#print(AXP)
FDX  = Stock_FDX[['Date','High']]
FDX.rename(columns={'High': 'FDX'}, inplace=True)
GOOGL  = Stock_GOOGL[['Date','High']]
GOOGL.rename(columns={'High': 'GOOGL'}, inplace=True)
IBM  = Stock_IBM[['Date','High']]
IBM.rename(columns={'High': 'IBM'}, inplace=True)
KO  = Stock_KO[['Date','High']]
KO.rename(columns={'High': 'KO'}, inplace=True)
MS  = Stock_MS[['Date','High']]
MS.rename(columns={'High': 'MS'}, inplace=True)
NOK  = Stock_NOK[['Date','High']]
NOK.rename(columns={'High': 'NOK'}, inplace=True)
XOM  = Stock_XOM[['Date','High']]
XOM.rename(columns={'High': 'XOM'}, inplace=True)
YHOO  = Stock_YHOO[['Date','High']]
YHOO.rename(columns={'High': 'YHOO'}, inplace=True)


#FDX, GOOGL, IBM, KO, MS, NOK, XOM, YHOO,
DATA=pd.merge(AAPL, AXP,  on='Date')
DATA=pd.merge(DATA, FDX, on='Date')
DATA=pd.merge(DATA, GOOGL,  on='Date')
DATA=pd.merge(DATA, IBM,  on='Date')
DATA=pd.merge(DATA, KO,  on='Date')
DATA=pd.merge(DATA, MS,  on='Date')
DATA=pd.merge(DATA, NOK,  on='Date')
DATA=pd.merge(DATA, XOM,  on='Date')
STOCK=pd.merge(DATA, YHOO,  on='Date')
pd.set_option('display.max_rows', None)
print(type(STOCK['Date']))


#make a plot of all stock during the period
#matplotlib.style.use('ggplot')

#plt.plot(STOCK['Date'], STOCK['AAPL'])
#plt.plot(period, Long_term_investment)
#plt.legend(['AAPL'], loc='upper left')
#plt.xlabel('Period')
#plt.ylabel('Stock')
#plt.title('Stock Price Evolution')
#plt.grid(True)
#plt.savefig(os.path.abspath('./Stock.png'))
#plt.show()