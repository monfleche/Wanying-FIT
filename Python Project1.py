################################################################################################
##
##  Python Project
##  Master 2 FIT
##  Wanying ZHAO & Amadou DJIBO
##
#################################################################################################


#import packages



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

#Plot Investement Evaluation
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy


N = 500
random_x = [0,1,2,3,4,5,6,7,8]
random_y = [8,7,6,5,4,3,2,1,0]

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

py.iplot(data, filename='basic-line')
