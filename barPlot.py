import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

# pip install pandas

plt.style.use('fivethirtyeight')

# with open('data.csv') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
        
#         language_counter = Counter()

#         for row in csv_reader:
#                 language_counter.update(row['LanguagesWorkedWith'].split(';'))

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
        language_counter.update(response.split(';'))
        
languages = []
popularity = []

# info is in tuples
for item in language_counter.most_common(15):
        languages.append(item[0])
        popularity.append(item[1])

# reverses in-place
languages.reverse()
popularity.reverse()

# barh makes it horizontal
plt.barh(languages, popularity)

plt.title("Most Popular Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()  

plt.savefig('horizontal_bar_graph.png')

plt.show()

###############################################################################

# # Median Dev Salaries by Age
# ages_x = list(range(25, 36))

# # creates a list counting with 0 as a numpy array
# x_indexes = np.arange(len(ages_x))    
# width = 0.25

# # Median Dev Salaries for the ages
# dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# # Median Python Dev Salaries by Age
# py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# # # Median JavaScript Dev Salaries by Age
# js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 75683]

# plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All Devs')

# # we can still use plot if we want to
# plt.bar(x_indexes, py_dev_y, width=width, label='Python')

# plt.bar(x_indexes + width, js_dev_y, width=width, label='JavaScript')



# plt.legend()

# # x indexes are the ticks and the label themselves are the ages
# plt.xticks(ticks=x_indexes, labels=ages_x)

# plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")
# plt.title("Median Salary (USD) by Age")

# plt.tight_layout()   # adds padding which helps with formatting on diff devices

# plt.show()