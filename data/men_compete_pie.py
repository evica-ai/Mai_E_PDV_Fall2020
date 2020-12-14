import matplotlib.pyplot as plt

# generate all medals that Canada men have won (386)

values = [192, 128, 66]
colors = ['light gold', 'silver', 'light brown']
labels = ["Gold", "Silver", "Bronze"]

explode = [0.1, 0.1, 0.1]
plt.pie(values, labels=labels, colors=colors, explode=explode)

plt.show()