################## This is a simulation of historic stock and bond market returns driven by user input to calculate scenarios with a set amount of money over a specific timeframe ################
#### Importing modules and data tools for better analysis
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
Inflation_Rate = df.Inflation_Rate.to_list()
Stock_ROR=[float(i) for i in ROR_stock]
Bond_ROR = [float(i) for i in ROR_bond]
Inflation_rate = [float(i) for i in Inflation_Rate]

#### Get Input from user

while True:
    try:
        TS = float(input("How much money would you like to invest in stocks: "))
    except ValueError:
        print("Can you please input the amount as a number, for example 1,000 as 1000, thank you!")
        continue
    if (TS < 0):
        print("Investments must be positive, please enter a number again, thank you!")
    else:
        break
while True:
    try:
        TB = float(input("How much money would you like to invest in bonds: "))
    except ValueError:
        print("Can you please input the amount as a number, for example 1,000 as 1000, thank you!")
        continue
    if (TB < 0):
        print("Investments must be positive, please enter a number again, thank you!")
    else:
        break
while True:
    try:
        TT = float(input("For how long are you planning to hold your investments in years: "))
    except ValueError:
        print("Sorry, input must be a number for processing, for example nine as 9, thank you!")
        continue
    if (TT <= 0):
        print("To calculate an investment return, year(s) must be one or greater, please enter a number greater than zero, thank you!")
    else:
        break
#### Defining functions that will randomly choose historical rates from the data sets
#### and apply them to balance for the trials of our Rate of Return simulation.

def stocks(inital_balance):
    rate = random.choice(Stock_ROR)
    return inital_balance * rate

def bonds(inital_balance):
    rate = random.choice(Bond_ROR)
    return inital_balance * rate

def inflation(inital_balance):
    rate = random.choice(Inflation_rate)
    return inital_balance * abs(rate)
#### Set inital conditions
number_years = TT
number_sims = 100000
final_balances_S = []
final_balances_B = []
for i in range(number_sims):
    time = 0
    balance_S = TS
    balance_B = TB
    while (time < number_years):
#### Increase balance and time
        balance_S += stocks(balance_S)
        balance_B += bonds(balance_B)
        balance_S -= inflation(balance_S)
        balance_B -= inflation(balance_B)
        time += 1
#### store time and balance in lists
    final_balances_S.append(balance_S)
    final_balances_B.append(balance_B)
#### Output the simulation results

final_S_average = np.mean(final_balances_S)
final_S_std = np.std(final_balances_S)
print("The average ending balance for stocks was ",round(final_S_average, 2),)
print("The standard deviation for stocks was ",round(final_S_std, 2))
final_B_average = np.mean(final_balances_B)
final_B_std = np.std(final_balances_B)
net_total = round(final_B_average + final_S_average, 2) - (TS + TB)
print("The average ending balance for bonds was ",round(final_B_average, 2))
print("The standard deviation for bonds was ",round(final_B_std, 2))
print("The average net earnings for stocks and bonds was", round(net_total,2), "or",round(net_total/TT, 2), "per year after inflation")

#### Graph to visualize the Spread
hist([final_balances_S, final_balances_B],bins = 40)
xlabel("Return value of Stocks and Bonds after a period of years")
ylabel("# of Times Returned")
title("Simulation of Investment Returns")
legend(["Stocks", "Bonds"])
show()

