import matplotlib.pyplot as plt

# generate all medals that Canada women have won (240)

values = [123, 27, 42]
colors = ['light gold', 'silver', 'light brown']
labels = ["Gold", "Silver", "Bronze"]

explode = [0.1, 0.1, 0.1]
fig1, ax1 = plt.subplots()
ax1.pie(values, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()