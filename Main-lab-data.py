#Plot for gas price comparisons (1)

import pandas as pd
import matplotlib.pyplot as plt 
import json

plt.figure(figsize=(8,5))

gas = pd.read_csv('Project_02/gas_prices.csv')

plt.title('Gas Prices over the years (in USD)', fontdict={'fontweight':'bold','fontsize':14})

plt.plot(gas['Year'], gas['USA'], 'b.-', label='United States',)
plt.plot(gas['Year'], gas['UK'], 'r.-', label='United Kingdom')
plt.plot(gas['Year'], gas['South Korea'], 'g.-', label='South Korea')
plt.plot(gas['Year'], gas['Germany'], 'o-', label='Germany')
plt.plot(gas['Year'], gas['Japan'], 'p-', label='Japan')


plt.xticks(gas.Year[::3],rotation=25)

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend()

plt.show()


#Plot for USA GDP (2)

us_gdp = []
text = ''
with open('Project_02/USA.GDP.json') as f:
    text = f.read()
us_gdp = json.loads(text)

gdp_value = {}
for year in range(1960,2021):
    gdp_value[year] = 0
    gdp_value[year] = us_gdp[1][year-1960]['value']

xs = sorted(gdp_value.keys())
ys = [ gdp_value[key] for key in xs ]


fig, ax = plt.subplots()
plt.xlabel('Year')
plt.ylabel('Gross Domestic Product Value (dollars in trillions)')
plt.title ('The decline of the USA GDP from 1960 - 2020', fontdict={'fontweight':'bold','fontsize':14})
ax.bar (xs, ys)
plt.show()


