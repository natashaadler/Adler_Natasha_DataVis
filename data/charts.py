import  matplotlib.pyplot as plt

# time frame
years = [1900, 1950, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2010, 2015]

#population
pops = [1.6, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5]

#plots a built in method / 
plt.plot(years, pops, color=(255/255, 150/255, 100/255), linewidth=4.0)
plt.ylabel("Population by Billions")
plt.xlabel("Groth By Year")
plt.title("Global Population Growth By Year")
plt.show()