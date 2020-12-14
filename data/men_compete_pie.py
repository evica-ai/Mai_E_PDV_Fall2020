import matplotlib.pyplot as plt


# generate all medals that Canada men have won (386)

values = [192, 128, 66]
colors = ['light gold', 'silver', 'light brown']
labels = ["Gold", "Silver", "Bronze"]

explode = [0, 0.1, 0]
fig1, ax1 = plt.subplots()
ax1.pie(values, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()