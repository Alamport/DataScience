from matplotlib import pyplot as plt
# stackplots are important when ur trying to track total and breakdown of total of individuals
# it is also good for visualizing something that maintains a constant total (team can only contribute 8 hrs on a project a day --> who contributes the most)

plt.style.use('fivethirtyeight')

# minutes = list(range(1, 10))
days = list(range(1, 10))

# player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
# player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
# player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
worker1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
worker2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
worker3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]


# pie chart of the first minute
# plt.pie([1, 1, 1], labels=["Player 1", "Player 2", "Player 3"])

labels = ["Player1", "Player2", "Player3"]
colors = ['#6d904f', '#fc4f30', '#008fd5']

# x axis
# plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)
plt.stackplot(days, worker1, worker2, worker3, labels=labels, colors=colors)


plt.title("My Awesome Stack Plot")

# loc gets the location of the legend
# plt.legend(loc='upper left')
# plt.legend(loc='lower left')
plt.legend(loc=(0.07, 0.05))    # bot left of legend is 7% from left & 5% bot
plt.tight_layout()

plt.savefig('stack_plot.png')
plt.show()