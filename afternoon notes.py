# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 14:22:22 2023

@author: Bogdan Tudose
"""

#Lesson 3
#%% Section 8 - Functions
    #to quickly repeat your analysis -->
            #you can make your own formulas

#formulas that outputs the cube of a number
    #def funcName(inputs):
        #calcs
        #return output

def fnCube(x):
    return x ** 3

def cagr(years, begVal, endVal):
    return (endVal/begVal)**(1/years) - 1
    #compounded annual growth rate


b = 100
e = 200
n = 5
r = cagr(n, b, e)
print(r) #15%
fnCube(6)

#%% Section 9 - Numpy
    #package for mathematical calcs
        #sum, max, min, std, cov, var, etc.
    #used for random numbers
        #to simulate data
    #matrix calcs
    #introduces a new data type:
            #numpy array --> more powerful list
            #matrix calcs with them
import numpy as np
pricesUSD = [100, 200, 50]
fx = 1.35
# pricesUSD * 2 #this repeats the list 2x
#can convert lists into an arry, then do matrix math
pricesCAD = np.array(pricesUSD) * fx

sales = [100, 50, 200]
costs = [90, 40, 180]
profits = np.array(sales) - np.array(costs)

dir(profits)
profits.sum()
profits.max()
# sales.max() #this doesn't work, it's a numpy method, only on array

np.sum(profits) #this works, using a function on list
 

#%% Section 10 - Pandas

#import data
#clean up
#"explore" - accessing data
# stats, calcs
# sort & filtering

#new data type: DataFrame (fancy name for a table)

import pandas as pd
sp500 = pd.read_csv("StockData/SP500.csv")
finDeals = pd.read_excel("ExData/Data Manipulation Worksheet.xlsx")

#%% Exploration Formulas
finDeals.info()
    #if #s are jumping around either:
        #missing data
        #too much data (imported lines we don't care about)

    #datatype:
        #numbers --> float or int
        #dates --> datetime
        #anything else is object (text, or lists, etc.)
sp500.info()


# finDeals = pd.read_excel("ExData/Data Manipulation Worksheet.xlsx",
                         # skipfooter=11)
                             #delete the last 11 rows while importing

finDeals = pd.read_excel("ExData/Data Manipulation Worksheet.xlsx",
                         sheet_name="Financing Table Clean")
# finDeals.info()

#%% Accessing rows/cols
sp500.head() #first 5 rows
sp500.tail() #last 5 rows

first20 = sp500.head(20)

#access rows:  df.iloc[x:y] #iloc = integer location, row numbers
sp500.iloc[20:25] #  20 <= rowNum < 25
sp500.iloc[-10:] #last 10 rows

#access columns: similar to dictionaries, df['col header']
sp500['Close']
#multiple headers: df[list of col headers]
newTable = sp500[['Close','Date','Open']]
# cols = ['Close','Date']
# sp500[cols]

#   df.iloc[rows][cols]
sp500.iloc[0:5][['Date','Close']]


#Can change the index to make it easier to extract data

sp500 = pd.read_csv("StockData/SP500.csv",
                    parse_dates=['Date'],
                    index_col=['Date'])
sp500.info()
#using your new index: df.loc[row name]
sp500.loc['2013-10-08']['Close']    #VLOOKUP in excel
        #iloc vs loc, iloc uses row numbers, loc uses ur new index
sp500.iloc[6]['Close'] #same as above
# ('Finance','IPOs')

#Break until 3:45pm

sp500.loc['2015']
sp500.loc['2015-01-01':'2015-12-31'] #same as line above

sp500.loc['2015-12-24':'2015-12-29']
        #INCLUSIVE!! of the top end
#%% Calculations
stats = sp500.describe() 
stats.to_csv('Output/sp500 stats.csv')
stats.to_excel('Output/sp500 stats.xlsx')

#calcs:  df['new column'] = calc
sp500['Intraday Return'] = sp500['Close'] / sp500['Open'] - 1
            # (close - open) / open

sp500['Daily Return'] = sp500['Close'] / sp500['Close'].shift(1) - 1
        # (close today - close yesterday) / close yesterday
                # x1/x0 - 1

sp500['Returns'] = sp500['Close'].pct_change()
    #same as above
    
sp500['Returns'].max()
sp500['Returns'].min()
sp500.loc['2015':'2016'][['Returns','Close']].mean()
    # df.loc[rows][cols].method()
    
# sp500.mean()
#Quick graphs
# sp500.loc['2015']['Returns'].hist(bins=100)
sp500.loc['2015']['Close'].plot()
    #Tools --> Preferences --> Ipython console --> Graphics --> 
                    # change Inline in dropdwon to "Automatic"

#%% Filtering
        # df[conditions]
        # df[ (cond1) | (cond2) ] #or
        # df[(cond1) & (cond2)]
                    #BEDMAS --> brackets, exponents, division, mult, add, subst
filter1 = finDeals[finDeals['LEAD UNDERWRITER']=='Lehman Brothers']

cond1 = finDeals['LEAD UNDERWRITER']=='Lehman Brothers'
filter1 = finDeals[cond1]

#find all the "big" up days and down days for S&P500
    # less than -3% or more than 3%
filter2 = sp500[ (sp500['Returns']>=0.03)  | (sp500['Returns']<=-0.03)]    
cond1 = sp500['Returns']>=0.03
cond2 = sp500['Returns']<=-0.03
filter2 = sp500[cond1 | cond2]

#Question: can you add the condition to the table?
sp500['BIG UP DAY'] = sp500['Returns']>=0.03


# nums = [50, 100, 60, 20]
# import numpy as np
# numsArray = np.array(nums)
# numsArray > 60
sp500['Close'].plot() #this is using matplotlib package to plot

#Grouping data
pivot = finDeals.groupby(['LEAD UNDERWRITER'])['SIZE'].sum()
pivot = finDeals.groupby(['LEAD UNDERWRITER'])['SIZE'].agg(['sum','count'])

pivot = finDeals.groupby(['LEAD UNDERWRITER','INDUSTRY'])['SIZE'].agg(['sum','count'])

#Production/miniPandasAssignmentQuestions.py
# Production/miniPandasAssignmentSolution.py

#assignment 2 solutions:
    # Production/FinPandasSolutions.py


