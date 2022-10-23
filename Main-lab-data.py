#Plot for gas price comparisons (1)

import pandas as pd
import matplotlib.pyplot as plt 
import json 
import numpy 
import os

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
USAgdp = []
with open('Project_02/USA.GDP.json') as f:
        USA = f.read()
        USAgdp += json.loads(USA)
xs = []
indgdpy = []
for line in USAgdp[1]:
        xs.append(line['date'])
        indgdpy.append(line['value'])
xs.reverse()
indgdpy.reverse()



fig, ax = plt.subplots()
ax.bar(xs, indgdpy, label = 'USA')
plt.title('The increase of the US GDP from 1960 - 2021', fontdict={'fontweight':'bold','fontsize':14})    
plt.xlabel('Year') 
plt.xticks(rotation=25) 
plt.xticks(numpy.arange(0, len(xs)+1, 5)) 
plt.ylabel('Gross Domestic Product (USD)') 
plt.legend()
plt.show()



