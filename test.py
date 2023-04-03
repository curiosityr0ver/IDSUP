from matplotlib import pyplot as plt

yrs = [1970, 1980, 1990, 2000, 2010, 2020, 2030]
gdp = [1075, 2018, 3076, 3092, 4012, 4045, 4053]
plt.plot(yrs, gdp)
plt.xlabel("Years")
plt.ylabel("Billions of USD ($)")
plt.title("GDP Growth over decades", {'size': '20', 'color':'Black', 'weight':'800'})

