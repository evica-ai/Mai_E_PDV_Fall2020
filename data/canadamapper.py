import matplotlib.pyplot as plt

hfont = { 'fontname' : 'Merriweather oblique'}
# plot/chart Canada gold medals

years = [1924, 1928, 1932, 1948, 1952, 1960, 1964, 1968, 1976, 1984, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

medals = [9, 12, 14, 18, 16, 3, 4, 1, 1, 2, 4, 3, 14, 53, 29, 68, 63]

plt.plot(years, medals, color=(150/225, 100/225, 100/225), linewidth=3.0)

# labels
plt.ylabel("No. of Gold Medals Won")
plt.xlabel("Medals Won Each Year")
plt.title("The Number of Gold Medals Canada has Won from 1924-2014", **hfont)

plt.show()