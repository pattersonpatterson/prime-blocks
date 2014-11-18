# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 15:31:42 2014

@author: derpson
"""

# imports
import pyprimes as prime
import pandas as pd
import numpy as np
import random as rn

############### Getting data and arranging in Data.Frame
# Take in value and check that it's not such a huge number
num = abs(int(raw_input("Give me a number: ")))
while (num>= 1000000000000):
    num = int(raw_input("Give me a smaller number (<1,000,000,000,000): " ))
    
# Find prime factorization of number and store factors (not 1) in DataFrame
data = prime.factors(num)
df = pd.DataFrame(data, columns=["prime"])

# Randomly generate int(x,y) positions for each factor (bound to 10, maybe 7)
# Positions must be unique in either x or y
# This could be cleaner
x=[]
y=[]
for factor in data:
    xcoord = rn.randint(0,10)
    ycoord = rn.randint(0,10)
    x.append(xcoord)
    y.append(ycoord)

# Check for uniqueness (???)

# Add coords to df
df['x'] = x
df['y'] = y

# Generate width for each factor as a multiple of factor in a logarithmic scale
# All heights = 0.9
'''For Now these will be all the same height and all the same width: 0.9'''

# Assign specific colors to each prime factor (only need 8)
colors = [
    'DarkOrange',
    'DeepSkyBlue',
    'Yellow',
    'Purple',
    'Salmon',
    'Lime',
    'Peru',
    'LightPink'
]

for unique_prime in set(data):


############### Display 
# Insert data into ColumnDataSource


# hold() to put all the boxes on one grid

# Make a rect glyph for each factor


# Add text to display the number for each box


# turn off grid lines - bk.grid().grid_line_color = None

# show the chart

