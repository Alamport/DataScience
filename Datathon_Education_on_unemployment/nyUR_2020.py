###############################################################################
# nyUR_2020.py                                    
#
# The program aims to find the association between locations in a specific 
# state (NY) with unemployment rates. Using this information, a further study
# can be condued to analyze the specific counties (in NY) that have high or
# low unemployment rates. One can wonder, does the type of area (UIC) have any
# affect on unemployment rates?
#
# Adin Lamport (March, 2024)
###############################################################################
import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv('Datathon_Education_on_unemployment/unemployment.csv')

columns_of_interest = [
        'FIPS_Code',
    'Unemployment_rate_2000',
    'Unemployment_rate_2001',
    'Unemployment_rate_2002',
    'Unemployment_rate_2003',
    'Unemployment_rate_2004',
    'Unemployment_rate_2005',
    'Unemployment_rate_2006',
    'Unemployment_rate_2007',
    'Unemployment_rate_2008',
    'Unemployment_rate_2009',
    'Unemployment_rate_2010',
    'Unemployment_rate_2011',
    'Unemployment_rate_2012',
    'Unemployment_rate_2013',
    'Unemployment_rate_2014',
    'Unemployment_rate_2015',
    'Unemployment_rate_2016',
    'Unemployment_rate_2017',
    'Unemployment_rate_2018',
    'Unemployment_rate_2019',
    'Unemployment_rate_2020'
]

filtered_data = data[data['State'] == 'NY']
unemployment_rate_NY = filtered_data[columns_of_interest]

year = list(range(2000, 2021))

# plots the data
plt.bar(list(unemployment_rate_NY['FIPS_Code']), list(unemployment_rate_NY['Unemployment_rate_2000']), )

# sets up the graph itself
plt.title("Unemployment Rate (2020) of different areas in NY")
plt.ylabel("Unemployment Rate")
plt.xlabel("FIPS_Code")

plt.tight_layout()  

# plt.savefig('Unemployment_Rate_NY_2020.png')
plt.show()