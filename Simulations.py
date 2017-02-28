import PythonProjectWZAD as market
from datetime import date
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import os
import dis
import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from random import randint


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

myyear = AverageDefensiveInvestor['year']
mydefencive= AverageDefensiveInvestor['Investment']
myaggressive = AverageAggressiveInvestor['Investment']
mymixed=AverageMixedInvestor['Investment']

# Create traces
trace0 = go.Scatter(
    x = myyear,
    y = mydefencive,
    line = dict(color = ('rgb(205, 12, 24)'),width = 4),
    name = 'Defensive'
)
trace1 = go.Scatter(
    x = myyear,
    y = myaggressive,
    line=dict(color=('rgb(22, 96, 167)'), width=4),
    name = 'Aggressive'
)
trace2 = go.Scatter(
    x = myyear,
    y = mymixed,
    line=dict(color=('rgba(49,130,189, 1)'), width=4),
    name = 'Mixed'
)
data = [trace0, trace1, trace2]
plotly.offline.plot(data, filename='Investment')



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
print(AverageMixedInvestor)