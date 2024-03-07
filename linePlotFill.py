import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data_1.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

# fills from py_salaries all the way to y2 = 0
# alpha refers to how much you can see through the color
# where is a conditional and does the fill when it's true
# interpolate makes sure certain x areas don't get clipped
# plt.fill_between(ages, py_salaries, alpha = 0.25)
plt.fill_between(ages, py_salaries, dev_salaries, 
                 where=(py_salaries > dev_salaries), 
                 interpolate=True, alpha = 0.25, label='Above Avg')

plt.fill_between(ages, py_salaries, dev_salaries, 
                 where=(py_salaries <= dev_salaries), 
                 interpolate=True, alpha = 0.25, label='Below Avg')

# plt.fill_between(ages, py_salaries, dev_salaries, interpolate=True, alpha = 0.25)


plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.savefig('line_plot_fill.png')

plt.show()