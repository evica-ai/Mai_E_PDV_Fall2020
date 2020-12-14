import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# data
medals = ("Gold Medals", "Silver Medals", "Bronze Medals")
y_pos = np.arange(len(medals))
performance = [315, 203, 107]
colors = ['light gold', 'silver', 'light brown']
error = np.random.rand(len(medals))


ax.barh(y_pos, performance, xerr=error, color=['gold', 'silver', 'brown'], align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(medals)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('No. of Medals Won')
ax.set_title('The Total Amount of Medals Won by Cananda')

plt.show()