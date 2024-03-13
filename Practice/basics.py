from matplotlib import pyplot as plt
# pip install matplotlib

plt.xkcd()      # xkcd comic style

# plt.style.use('ggplot')
# print(plt.style.available)
# fivethirtyeight
# seaborn
# ggplot

# Median Dev Salaries by Age
ages_x = list(range(25, 36))

# Median Dev Salaries for the ages
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Median Python Dev Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Dev Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 75683]

# plots the two lists
# home / undo / redo / move / zoom / config / save

# hex color
plt.plot(ages_x, py_dev_y, label='Python')
# plt.plot(ages_x, py_dev_y, color='#5a7d9a', linewidth=3, label='Python')
        # plt.plot(ages_x, py_dev_y, "b", label = "Python")

plt.plot(ages_x, js_dev_y, label='JavaScript')
# plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JavaScript')


plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs')
        # plt.plot(ages_x, dev_y, "k--", label = "All Devs")

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")

# plt.legend(["All Devs", "Python"])    # kinda error prone as it relies on the coder rememebering the order
plt.legend()

# plt.grid(True)  # adds grid

plt.tight_layout()   # adds padding which helps with formatting on diff devices

# saves figure in depository (or location if u write so)
plt.savefig('plot.png')

plt.show()