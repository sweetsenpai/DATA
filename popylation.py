import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
pops = [2525, 2758, 3018, 3322, 3682, 4061, 4440, 4853, 5310, 5735, 6127, 6520, 6930, 7349]
i = 0
deaths = [1.2, 1.3, 2.2, 2.5, 2.8, 2.9, 4.6, 3.0, 5.4, 4.6, 3.2, 5.5, 6.9, 7.8]
for pop in pops:
    pops[i] = round((pop / 1000), 1)
    i += 1

lines = plt.plot(years, pops, years, deaths)
plt.grid(True)#сетка
plt.setp(lines, color=(1, .4, .4), marker="o")
"""
plt.plot(years, pops, color=(12/255, 223/225, 118/225))
plt.plot(years, deaths, "--", color=(.6, .6, 1))
plt.title("Рост населения земли")
plt.xlabel("Население в год")
plt.ylabel("Население в млн.")
"""
plt.show()
