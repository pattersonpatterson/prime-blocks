# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 15:31:42 2014

@author: derpson
"""

# imports
import pyprimes as prime
import pandas as pd
import random as rn
import bokeh.plotting as bk
from bokeh.objects import ColumnDataSource

############### Getting data and arranging in Data.Frame
# Take in value and check that it's not such a huge number
num = abs(int(raw_input("Give me a number: ")))
while (num>= 1000000000000):
    num = int(raw_input("Give me a smaller number (<1,000,000,000,000): " ))
    
# Find prime factorization of number and store factors (not 1) in DataFrame
data = prime.factors(num)
df = pd.DataFrame(data, columns=["prime"])

# Output to html
bk.output_file("primes.html", title="Prime Factor Visualization")

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

del x,y

# Generate width for each factor as a multiple of factor in a logarithmic scale
# All heights = 0.9
'''For Now these will be all the same height and all the same width: 0.9'''

# Assign specific colors to each prime factor (only need 8)
colors = [
    'DarkOrange',
    'DeepSkyBlue',
    'Purple',
    'Salmon',
    'Yellow',    
    'Lime',
    'Peru',
    'LightPink',
    'Teal'
]

cmap = dict(zip(df['prime'].unique(),colors))
df['color'] = df['prime'].replace(cmap)

############### Display 
# Insert data into ColumnDataSource
source = ColumnDataSource(
    data = dict(
        xpos = [str(x) for x in df['x']],
        ypos = [str(y) for y in df['y']],
        number = df['prime'],
        color_prime = df['color']
    )
)

# hold() to put all the boxes on one grid
bk.hold()

# Set x-y ranges
x_range = [str(x) for x in range(-1,11)]
y_range = [str(y) for y in range(-1,-11)]
# Make a rect glyph for each factor
bk.rect("xpos","ypos",0.9,0.9,source=source,
        x_range=x_range, y_range=y_range,
        fill_alpha=0.6, color="color_prime",
        tools="resize", title="Prime Factor Visualization"
)

# Add text to display the number for each box
# Use text_props = dict to set properties of text elements
text_props = {
    "source": source,
    "angle": 0,
    "color": "black",
    "text_align": "center",
    "text_baseline": "middle"
}

bk.text(x=dict(field="xpos", units="data"),
     y=dict(field="ypos", units="data"),
     text=dict(field="number", units="data"),
     text_font_style="bold", text_font_size="12pt", **text_props)

# turn off grid lines - bk.grid().grid_line_color = None
bk.grid().grid_line_color = None
# show the chart
bk.show()
