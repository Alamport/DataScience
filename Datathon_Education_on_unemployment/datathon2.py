import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv('unemployment.csv')

columns_of_interest = [
        'Unemployment_rate_2000',
        'Unemployment_rate_2001',
        'Unemployment_rate_2002',
        'Unemployment_rate_2003',
]

us_unemployments = []
usa_data = data[data['Area_name'] == 'United States']
us_unemployment = usa_data[columns_of_interest]
us_unemployments.append(list(us_unemployment['Unemployment_rate_2000']))
us_unemployments.append(list(us_unemployment['Unemployment_rate_2001']))
us_unemployments.append(list(us_unemployment['Unemployment_rate_2002']))
us_unemployments.append(list(us_unemployment['Unemployment_rate_2003']))

print(list(us_unemployment['Unemployment_rate_2000']))
unemployment_percent_change = [0]
index = 1
while (index < 4):
        percent_change = (us_unemployments[index][0] - us_unemployments[0][0]) / us_unemployments[0][0]
        percent_change *= 100
        unemployment_percent_change.append(round(percent_change, 2))
        index += 1

print(unemployment_percent_change)


x_axis = [2000, 2001, 2002, 2003]
# percent change in unemployment
y_axis = unemployment_percent_change

plt.plot(x_axis, y_axis)

plt.xticks(x_axis) 

plt.title("% Change in Unemployment Rate (2000 - 2003)")
plt.xlabel("Years")
plt.ylabel("Percent Change")

plt.tight_layout()  

plt.show()
