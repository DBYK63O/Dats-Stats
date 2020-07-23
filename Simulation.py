#### Importing modules and data tools for better anaylsis
import random
import pandas as pd
import numpy as np
from matplotlib.pyplot import hist, show, xlabel, ylabel, legend, title

#### Importing historic stock and bond market data from 1928 -2019 showing annual returns

column_names = ["year", "stocks", "T.Bill",	"Bond",	"Corporate_Bond", "Inflation_Rate"]
df = pd.read_csv("ROR.csv", names = column_names)
#### Cleaning the data and putting it into readable lists for python
ROR_stock = df.stocks.to_list()
ROR_bond = df.Bond.to_list()
Stock_ROR=[float(i) for i in ROR_stock]
Bond_ROR = [float(i) for i in ROR_bond]
# print(Stock_ROR)
# print(Bond_ROR)


#### Defining functions that will randomly choose historical rates from the data sets
#### and apply them to balance for the trials of our Rate of Return simulation.

def stocks(inital_balance):
    rate = random.choice(Stock_ROR)
    return inital_balance * rate

def bonds(inital_balance):
    rate = random.choice(Bond_ROR)
    return inital_balance * rate
#### Set inital conditions
number_years = 10
number_sims = 10000
final_balances_S = []
final_balances_B = []
for i in range(number_sims):
    time = 0
    balance_S = 1000
    balance_B = 1000
    while (time < number_years):
#### Increase balance and time
        balance_S += stocks(balance_S)
        balance_B += bonds(balance_B)
        time += 1
#### store time and balance in lists
    final_balances_S.append(balance_S)
    final_balances_B.append(balance_B)
#### Output the simulation results

final_S_average = np.mean(final_balances_S)
final_S_std = np.std(final_balances_S)
print("The average ending balance for stocks was ",round(final_S_average, 2))
print("The standard deviation for stocks was ",round(final_S_std, 2))
final_B_average = np.mean(final_balances_B)
final_B_std = np.std(final_balances_B)
print("The average ending balance for bonds was ",round(final_B_average, 2))
print("The standard deviation for bonds was ",round(final_B_std, 2))

#### Graph to visualize the Spread
hist([final_balances_S, final_balances_B],bins = 40)
xlabel("Return value of $1000 after a 10 year period")
ylabel("# of Times Returned")
title("Simulation of Investment Returns")
legend(["Stocks", "Bonds"])
show()