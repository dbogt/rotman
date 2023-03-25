# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 08:53:02 2023

@author: Bogdan Tudose
"""
#Rotman Commerce - Python 1 with Marquee Group
#Bogdan Tudose
#bogdan.tudose@marqueegroup.ca
#Python Demos: https://bogdan.streamlit.app/

# Before we get started:
#     1) please make sure to download and install Anaconda
                # https://www.anaconda.com/products/distribution
#     2) please download and unzip course materials:
#         https://marqueegroup.ca/event/iny92/
#     3) open up Spyder:
#             from Anaconda Navigator (launch Spyder) 
#             or
#             in Anaconda Prompt, type "spyder" then hit Enter
    
#     don't worry about updating conda for today's class
    
# Spyder Settings:
        # View --> Window Layouts --> Rstudio
#Projects --> New Project
    #browse to "Python Project" folder that you unzipped
    
    
    
#%% Section 1 - Intro to Spyder
    #Running your code
        #F9 --> rune one line at a time (or multiple selected)
        #CTRL/SHIFT + ENTER --> run a section (cell block)
        #F5 --> run the entire file (don't use today)

#%% Section 2 - Data Types

firstName = "Bogdan" #string
lastName = 'Tudose'
x = 5   #int
y = 2.2 #float --> #s with decimals
greeting = "Hello World"

longText = ''' text
going on
multiple
lines of
code '''

fullName = firstName + " " + lastName
        #to attach strings use +
        #concatenating

# '5' + 5 # '55' OR 10??
# 5 + '5'

#Slide 14 - data types cheat sheet

print(int('5') + 5) #10
str(5) + '5' # '55'

    #to output results either use print(output)
    #or hit f9 on the line of code

#%% Section 3 - Strings
greeting = "Hello World"

#extracting characters
    #similar LEFT, RIGHT, MID in Excel
#python: variable[x:y] --> extracts x <= charNum < y

greeting[0:5] # 'Hello'
    #counting starts at 0
    # 0 <= char < 5

greeting[7:9] # "or"
greeting[-5:] #last 5 characters
        # "World"

greeting[6] #'W'

#String Methods
# Functions vs Methods
#Methods - special formulas you can ONLY use on
            #ONE datatype (or object)
            #  variable.method()
            
#Function - generic formula, can use on multiple data types
    # function(input)

print("5") #function
type(6.5) #function
greeting.upper() #string method

dir("text") #directory
# greeting.

messyNum = "$123,456"
messyNum * 2 #replicates the text

messyNum.strip("$")
    #this is temporary, doesn't modify the original var
messyNum = messyNum.strip("$")

messyNum = messyNum.replace(',', '')
messyNum = int(messyNum)

messyNum = "$123,456"
messyNum = int(messyNum.strip("$").replace(",",''))

#%% Coffee Break until 10:45am
    #let me know if any issues opening up spyder
    #Notes so far in Lesson 1

#%% Section 4 - Lists and List Methods
# lists allow storing multiple data in same variable
# arrays in other coding languages
# matrix

#inefficient
ticker1 = "AAPL"
ticker2 = "MSFT"
ticker3 = "NFLX"

#more efficients
tickers = ['AAPL', 'MSFT', 'NFLX']
companies = ['Apple','Microsoft','Netflix']
prices = [160.25, 280.57, 328.39]

stockData= [['AAPL','Apple',160.25],
            ['MSFT','Microsoft',280.57]]

#extract data --> similar to strings
stockData[0][-1] # 160.25
tickers[0] # 'AAPL'
prices[0:2]

#modify data
companies[0] = "Apple Inc."
dir(tickers)

#adding data
tickers.append("SHOP")
companies.append("Shopify")

tickers.insert(2,'NVDA')
companies.insert(2, "NVIDIA")

#removing data
tickers.remove("SHOP")
tickers.pop(2)

#%% Section 5 - Dictionaries & Tuples
#Lesson 2 
#dictionaries --> similar to lists, but you can "name" the "rows"
    #dictName = {'key':value, 'key':value, ....}
        #keys --> are the names for the index
        #keys have to be unique
        #they're not sorted/ordered when storing in memory
stockData = {'MSFT':280.57,
             'AMZN':{'Price':98.13, 'Company':'Amazon','EPS':2.51},
             'NFLX':328.39,
             'SHOP':61.73}

#Extracting & modifying data
stockData['AMZN']['EPS'] #2.51
stockData['NFLX'] #328
stockData['NFLX'] = 335

#Adding data
stockData['TSLA'] = 190.41


dir(stockData)

stockData.keys() #list of just the keys
stockData.values() #list of just the values

dir(stockData)
stockData.pop('TSLA')

#%%% Tuple
    #arrays to store constants
    #exact same thing as a list, but they're immutable
        #you can't change them once you create them
        #can't add/delete data or modify data
        #tupleName = (value1, value2, ...)
taxRates = (0.15, 0.40, 0.52)
taxRates[0]

#taxRates[0] = 0.18
# 'tuple' object does not support item assignment

#%% Section 6 - If Statements
#and / or 
    #and --> EVERYTHING has to be True --> True
    #or ---> at least ONE of the conditions needs to be True

# and --> &
# or --> |

#comparing two values -->  ==
#not equal to --> !=  (vs <> in excel)

x = 6
y = 6

if x > y: 
    print("x is greater than y") 
    print("x is",x)
elif x==6:
    print("x is 6")
elif x==y: #right now, this will not run
    print("x is equal to y")
else: #what runs if all of above is false
    print("y is greater")    
    
print("this is outside the if")

#%% Section 7 - Looping
    # lets you repeat code
    # two types:
            # for loop - you tell it how many times to run
            # while loop - runs using a condition (if stmt)

#%%% For Loop
#1) loop through a data set
#2) loop throug a range of numbers you pick

pricesUSD = [100, 90, 25, 16]
usdcad = 1.35
# pricesUSD[0] * usdcad
# pricesUSD[1] * usdcad
pricesCAD = [] #empty list

for price in pricesUSD: # x= 100, 90, 25, 16
    # print(price)
    # print(price * usdcad)
    pricesCAD.append(round(price * usdcad,4))
    print(pricesCAD)

print("this is outside loop")

#List Comprehension --> example in Lesson 2
    #can create a new list from old list in one step
    # newList = [calc for x in oldlist]
pricesCAD = [x*usdcad for x in pricesUSD]

#pick your own numbers with range(x) or range(x, y)
for x in range(100):
    print(x**2) #x^2 for all the numbers bw 0 to 100
            #  0<= x < 100

#%%% While Loop
    #for loop mixed with an if statement (condition)
    #loops keep running if cond is true

x = 10

#DO NOT RUN YET!!!
    #infinite loop
    #make sure your condition eventually becomes false
while x <= 100:
    print(x)
    # x = x + 10
    x += 10

#%% Assignment 1 --> #1-5
    #Lunch until 1pm
    #Working session until 1:30pm
    




