"""
Here we try to get option strike data and calculate the option greeks for a particular strike for current week.

"""


import pandas as pd
from nsefetch import *





niftyltp = rawdata['records']['underlyingValue']

#Rounding off the underlying to nearest 50 number to find ATM strike of the latest option chain
def atm_strike(n,m=50):
    a = (n // m) * m
    b = a + m
    return int(b if n - a > b - n else a)

nifty_atm= atm_strike(niftyltp)
print(nifty_atm)


#Calculating option greeks