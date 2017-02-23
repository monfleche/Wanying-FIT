################################################################################################
##
##  Python Project
##  Master 2 FIT
##  Wanying ZHAO & Amadou DJIBO
##
#################################################################################################


#import packages
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
        investment = self.minimum_amount*((1+self.yearly_interest_rate)**period)
        return investment

Short_term_bonds = Bonds(2, 1000, 0.01)
Long_term_bonds = Bonds(5, 3000, 0.05)

period=[]
Short_term_investment=[]
Long_term_investment=[]

for t in range(101):
    period.append(t)
    Short_term_investment.append(Short_term_bonds.CalculateInvestment(t))
    Long_term_investment.append(Long_term_bonds.CalculateInvestment(t))
print([period,Short_term_investment,Long_term_investment])

#optional style
matplotlib.style.use('ggplot')

plt.plot(period, Short_term_investment)
plt.plot(period, Long_term_investment)
plt.legend(['Short term', 'Long term'], loc='upper left')
plt.xlabel('Period')
plt.ylabel('Investment')
plt.title('Investment Revolution')
plt.grid(True)
plt.savefig(os.path.abspath('./BondsRevolution.png'))
plt.show()

##############Create Stocks#############
