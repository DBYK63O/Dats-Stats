import pandas as pd
import numpy as np
import random

# Gather data and calculate relevant stats
# TS = pd.read_csv("TSLA.csv")
# NQ = pd.read_csv("NASDQ.csv")
# avg_ts = np.mean(TS)
# std_ts = np.std(TS)
# avg_NQ = np.mean(NQ)
# std_NQ = np.std(NQ)
# print(avg_ts, std_ts, avg_NQ, std_NQ)

def RoRTSLA(inital_balance):
    rate = random.gauss(.504, .993)
    return inital_balance * rate

def RoRNQ(inital_balance):
    rate = random.gauss(.155, .137)
    return inital_balance * rate
number_years = 10
number_sims = 10000
final_balances_TS = []
final_balances_NQ = []
for i in range(number_sims):
    time = 0
    balance_TS = 1000
    balance_NQ = 1000
    while (time < number_years):
        balance_TS += RoRTSLA(balance_TS)
        balance_NQ += RoRNQ(balance_NQ)
        time += 1
    final_balances_TS.append(balance_TS)
    final_balances_NQ.append(balance_NQ)

#Output the simulation results

final_TS_average = np.mean(final_balances_TS)
final_TS_std = np.std(final_balances_TS)
# print(final_balances_average)
# print(final_balances_std)
final_NQ_average = np.mean(final_balances_NQ)
final_NQ_std = np.std(final_balances_NQ)
print("This data was based on the annual returns and standard deviation for the NASDAQ composite and TSLA motor company \n"
      "from the previous 10 years (2010 -2020). After running simulations of 10,000 trials based on these averages and assuming \n"
      "their continuation into the future with a Gaussian distribution we found an average return and standard deviation for TSLA was\n"
      ,round(final_TS_average, 2),"and", round(final_TS_std, 2), "respectivley, with a beginning balance of $1,000 after a 10 year \n"
      "period. In comparison to an average return of", round(final_NQ_average, 2), "and", round(final_NQ_std, 2), "of the NASDAQ composite \n"
      "during the same period.")


