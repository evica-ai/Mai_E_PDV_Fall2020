import matplotlib.pyplot as plt

# generate all medals that Canada women have won (240)

values = [123, 27, 42]
colors = ['light gold', 'silver', 'light brown']
labels = ["Gold", "Silver", "Bronze"]

explode = [0.1, 0.1, 0.1]
plt.pie(values, labels=labels, colors=colors, explode=explode)

plt.show()