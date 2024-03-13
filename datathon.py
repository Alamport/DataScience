import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv('unemployment.csv')

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
print(unemployment_rate_NY)
print("2000!")
print(list(unemployment_rate_NY['Unemployment_rate_2000']))
# print(filtered_data)

# unemployment_rate_2000 = data['Unemployment_rate_2000'][0]
# unemployment_rate_2001 = data['Unemployment_rate_2001'][0]
# unemployment_rate_2002 = data['Unemployment_rate_2002'][0]
# unemployment_rate_2003 = data['Unemployment_rate_2003'][0]
# unemployment_rate_2004 = data['Unemployment_rate_2004'][0]
# unemployment_rate_2005 = data['Unemployment_rate_2005'][0]
# unemployment_rate_2006 = data['Unemployment_rate_2006'][0]
# unemployment_rate_2007 = data['Unemployment_rate_2007'][0]
# unemployment_rate_2008 = data['Unemployment_rate_2008'][0]
# unemployment_rate_2009 = data['Unemployment_rate_2009'][0]
# unemployment_rate_2010 = data['Unemployment_rate_2010'][0]
# unemployment_rate_2011 = data['Unemployment_rate_2011'][0]
# unemployment_rate_2012 = data['Unemployment_rate_2012'][0]
# unemployment_rate_2013 = data['Unemployment_rate_2013'][0]
# unemployment_rate_2014 = data['Unemployment_rate_2014'][0]
# unemployment_rate_2015 = data['Unemployment_rate_2015'][0]
# unemployment_rate_2016 = data['Unemployment_rate_2016'][0]
# unemployment_rate_2017 = data['Unemployment_rate_2017'][0]
# unemployment_rate_2018 = data['Unemployment_rate_2018'][0]
# unemployment_rate_2019 = data['Unemployment_rate_2019'][0]
# unemployment_rate_2020 = data['Unemployment_rate_2020'][0]

year = list(range(2000, 2021))

# unemployment = [unemployment_rate_2000, unemployment_rate_2001, 
#                 unemployment_rate_2002, unemployment_rate_2003,
#                 unemployment_rate_2004, unemployment_rate_2005, 
#                 unemployment_rate_2006, unemployment_rate_2007,
#                 unemployment_rate_2008, unemployment_rate_2009, 
#                 unemployment_rate_2010, unemployment_rate_2011,
#                 unemployment_rate_2012, unemployment_rate_2013, 
#                 unemployment_rate_2014, unemployment_rate_2015,
#                 unemployment_rate_2016, unemployment_rate_2017, 
#                 unemployment_rate_2018, unemployment_rate_2019,
#                 unemployment_rate_2020]

# print(filtered_data.loc[:, 'Unemployment_rate_2000':'Unemployment_rate_2020'])
# unemployment2 = filtered_data.iloc[:, 11:79:4]
# print(unemployment2)
# language_counter = Counter()

# for response in lang_responses:
#         language_counter.update(response.split(';'))
        
# languages = []
# popularity = []

# # info is in tuples
# for item in language_counter.most_common(15):
#         languages.append(item[0])
#         popularity.append(item[1])

plt.bar(list(unemployment_rate_NY['FIPS_Code']), list(unemployment_rate_NY['Unemployment_rate_2000']), )

plt.title("Unemployment Rate (2020) of different areas in NY")
plt.ylabel("Unemployment Rate")
plt.xlabel("FIPS_Code")

plt.tight_layout()  

plt.savefig('Unemployment_Rate_NY_2020.png')
plt.show()