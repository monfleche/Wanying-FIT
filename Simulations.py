import PythonProjectWZAD as market
from datetime import date
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np

import datetime
import matplotlib

import random
import statistics


# Calculate the average investment of defensive investor type for each year
AverageDefensiveInvestor = []
for year in range(2005, 2015):
    enddate = date(year, 12, 31)
    AverageDefensiveInvestor.append([float(year), sum(market.DefensiveInvestor[i].defensive_Investement('20050101', enddate) for i in range(1, 1001)) / 1000])
AverageDefensiveInvestor = pd.DataFrame(AverageDefensiveInvestor)
AverageDefensiveInvestor.columns = ['year', 'Investment']

# Calculate the average investment of defensive investor type for each year
AverageAggressiveInvestor=[]
for year in range(2005, 2015):
    enddate = date(year, 12, 31)
    AverageAggressiveInvestor.append([float(year), sum(market.AggressiveInvestor[i].aggressive_Investment('20050103',  enddate) for i in range(1, 1001)) / 1000])
AverageAggressiveInvestor = pd.DataFrame(AverageAggressiveInvestor)
AverageAggressiveInvestor.columns = ['year', 'Investment']

#Calculate the average investement of mixed investor type for each year
AverageMixedInvestor=[]
for year in range(2005, 2015):
    enddate = date(year, 12, 31)
    AverageMixedInvestor.append([float(year), sum(market.MixedInvestor[i].mixed_Investment('20050103',  enddate) for i in range(1, 1001)) / 1000])
AverageMixedInvestor = pd.DataFrame(AverageMixedInvestor)
AverageMixedInvestor.columns = ['year', 'Investment']


##########################################################################
print('Plotting average investment evolution for three types of investors ')
myyear = AverageDefensiveInvestor['year']
mydefencive= AverageDefensiveInvestor['Investment']
myaggressive = AverageAggressiveInvestor['Investment']
mymixed=AverageMixedInvestor['Investment']

# Create traces
trace0 = go.Scatter(
    x = myyear,
    y = mydefencive,
    mode='lines+markers',
    name = 'Defensive'
)
trace1 = go.Scatter(
    x = myyear,
    y = myaggressive,
    mode='lines+markers',
    name = 'Aggressive'
)
trace2 = go.Scatter(
    x = myyear,
    y = mymixed,
    mode='lines+markers',
    name = 'Mixed'
)
data = [trace0, trace1, trace2]
layout = dict(title = 'Investment of three Investor types ',
              xaxis = dict(title = 'Period'),
              yaxis = dict(title = 'Investment'),
              )
fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='Investment.png')




#########################################################################################################################################
#####start budget *10 and run de previous code again
DefensiveInvestor = dict()
AggressiveInvestor = dict()
MixedInvestor = dict()
for i in range(1, 1001):
    DefensiveInvestor[i] = market.Defensive(120000, 'Defensive',120000)
    AggressiveInvestor[i] = market.Aggressive(120000, 'Aggressive',120000)
    MixedInvestor[i] = market.Mixed(120000, 'Mixed', 120000)

AverageDefensiveInvestor = []
for year in range(2005, 2015):
    enddate = date(year, 12, 31)
    AverageDefensiveInvestor.append([float(year), sum(market.DefensiveInvestor[i].defensive_Investement('20050101', enddate) for i in range(1, 1001)) / 1000])
AverageDefensiveInvestor = pd.DataFrame(AverageDefensiveInvestor)
AverageDefensiveInvestor.columns = ['year', 'Investment']

# Calculate the average investment of defensive investor type for each year
AverageAggressiveInvestor=[]
for year in range(2005, 2015):
    enddate = date(year, 12, 31)
    AverageAggressiveInvestor.append([float(year), sum(market.AggressiveInvestor[i].aggressive_Investment('20050103',  enddate) for i in range(1, 1001)) / 1000])
AverageAggressiveInvestor = pd.DataFrame(AverageAggressiveInvestor)
AverageAggressiveInvestor.columns = ['year', 'Investment']

#Calculate the average investement of mixed investor type for each year
AverageMixedInvestor=[]
for year in range(2005, 2015):
    enddate = date(year, 12, 31)
    AverageMixedInvestor.append([float(year), sum(market.MixedInvestor[i].mixed_Investment('20050103',  enddate) for i in range(1, 1001)) / 1000])
AverageMixedInvestor = pd.DataFrame(AverageMixedInvestor)
AverageMixedInvestor.columns = ['year', 'Investment']

###############plot againt with buget *10
print('Plotting average investment evolution for three types of investors - Larger buget')
myyear = AverageDefensiveInvestor['year']
mydefencive= AverageDefensiveInvestor['Investment']
myaggressive = AverageAggressiveInvestor['Investment']
mymixed=AverageMixedInvestor['Investment']

# Create traces
trace0 = go.Scatter(
    x = myyear,
    y = mydefencive,
    mode='lines+markers',
    name = 'Defensive'
)
trace1 = go.Scatter(
    x = myyear,
    y = myaggressive,
    mode='lines+markers',
    name = 'Aggressive'
)
trace2 = go.Scatter(
    x = myyear,
    y = mymixed,
    mode='lines+markers',
    name = 'Mixed'
)
data = [trace0, trace1, trace2]
layout = dict(title = 'Investment with larger budget',
              xaxis = dict(title = 'Period'),
              yaxis = dict(title = 'Investment'),
              )
fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='Investment with larger budget.png')



#######################################################################################################################################################################
##############################change investor budget randomly
#creat a sample with normal distrubution
budgetsample=np.random.normal(20000,5000,1000)
DefensiveInvestor = dict()
AggressiveInvestor = dict()
MixedInvestor = dict()
for i in range(1, 1001):
    rnd=random.choice(budgetsample)
    DefensiveInvestor[i] = market.Defensive(rnd, 'Defensive',rnd)
    rnd = random.choice(budgetsample)
    AggressiveInvestor[i] = market.Aggressive(rnd, 'Aggressive',rnd)
    rnd = random.choice(budgetsample)
    MixedInvestor[i] = market.Mixed(rnd, 'Mixed', rnd)
AverageDefensiveInvestor = []
for year in range(2005, 2015):
    enddate = date(year, 12, 31)
    AverageDefensiveInvestor.append([float(year), sum(market.DefensiveInvestor[i].defensive_Investement('20050101', enddate) for i in range(1, 1001)) / 1000])
AverageDefensiveInvestor = pd.DataFrame(AverageDefensiveInvestor)
AverageDefensiveInvestor.columns = ['year', 'Investment']

# Calculate the average investment of defensive investor type for each year
AverageAggressiveInvestor=[]
for year in range(2005, 2015):
    enddate = date(year, 12, 31)
    AverageAggressiveInvestor.append([float(year), sum(market.AggressiveInvestor[i].aggressive_Investment('20050103',  enddate) for i in range(1, 1001)) / 1000])
AverageAggressiveInvestor = pd.DataFrame(AverageAggressiveInvestor)
AverageAggressiveInvestor.columns = ['year', 'Investment']

#Calculate the average investement of mixed investor type for each year
AverageMixedInvestor=[]
for year in range(2005, 2015):
    enddate = date(year, 12, 31)
    AverageMixedInvestor.append([float(year), sum(market.MixedInvestor[i].mixed_Investment('20050103',  enddate) for i in range(1, 1001)) / 1000])
AverageMixedInvestor = pd.DataFrame(AverageMixedInvestor)
AverageMixedInvestor.columns = ['year', 'Investment']

###############plot againt with buget *10
print('Plotting average investment evolution for three types of investors - Random budget')
myyear = AverageDefensiveInvestor['year']
mydefencive= AverageDefensiveInvestor['Investment']
myaggressive = AverageAggressiveInvestor['Investment']
mymixed=AverageMixedInvestor['Investment']

# Create traces
trace0 = go.Scatter(
    x = myyear,
    y = mydefencive,
    mode='lines+markers',
    name = 'Defensive'
)
trace1 = go.Scatter(
    x = myyear,
    y = myaggressive,
    mode='lines+markers',
    name = 'Aggressive'
)
trace2 = go.Scatter(
    x = myyear,
    y = mymixed,
    mode='lines+markers',
    name = 'Mixed'
)
data = [trace0, trace1, trace2]
layout = dict(title = 'Investment with Random budget',
              xaxis = dict(title = 'Period'),
              yaxis = dict(title = 'Investment'),
              )
fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='Investment with Random budget.png')

################################################################################################################################################################
##############select the best stock on 2017
#the best stock is the stock with the highest average return and lowest variation
averagereturn=[]
variance=[]
endday = []
for i in range(0, 365):
    endday.append(date(2007, 1, 1) + datetime.timedelta(i))

for i in range (0,9):
        averagereturn.append([i,statistics.mean(market.stock_return(market.STOCK[i], '20070101', sellday) for sellday in endday)])
        variance.append([i,statistics.variance((market.stock_return(market.STOCK[i], '20070101', sellday) for sellday in endday))])
averagereturn=pd.DataFrame(averagereturn)
variance=pd.DataFrame(variance)
print(averagereturn)
print(variance)
#stock[0] Apple has the higher return but a high risk, and stock[1] American Express has a lowest variance, less risk but negative average return.  Depends on people risk version
#we can choose a good stock with high average return and low variance of return to invest


