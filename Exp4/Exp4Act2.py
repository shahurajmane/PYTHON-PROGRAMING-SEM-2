# Find total bill
"""
Created on Tue Mar 10 11:07:05 2026

@author: Shahuraj Mane
"""

n = int(input("Enter number of Products:"))
prices = []
for i in range(n):
    price = int(input("Enter prices:"))
    prices.append(price)
    total = sum(prices)
    print("total Bill =",total)
