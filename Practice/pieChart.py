from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# slices = [120, 80, 30, 20]
# labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']

# # blue, red, yellow, green
# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

# 10% of the radius out of the circle
explode = [0, 0, 0, 0.1, 0]

# matplotlib wedge for more info
# shadow makes it look 3D
# startangle can rotate the pie chart
# autopct gets the percentages of a pie chart

# plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})


plt.title("My Awesome Pie Chart")
plt.tight_layout()

plt.savefig('pie_chart.png')
plt.show()