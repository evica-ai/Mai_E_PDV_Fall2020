import matplotlib.pyplot as plt

hfont = { 'fontname' : 'Merriweather oblique'}
# plot/chart America gold medals

years = [1924, 1928, 1932, 1948, 1952, 1960, 1964, 1968, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

medals = [1, 6, 11, 8, 4, 2, 18, 1, 1, 6, 24, 4, 2, 5, 6, 25, 11, 9, 12, 10]

plt.plot(years, medals, color=(150/225, 100/225, 100/225), linewidth=3.0)

# labels
plt.ylabel("No. of Gold Medals Won")
plt.xlabel("Medals Won Each Year")
plt.title("The Number of Gold Medals America (United States of America) has Won from 1924-2014", **hfont)

plt.show()