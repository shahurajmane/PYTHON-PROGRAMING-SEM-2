# Find FActorial Number
"""
Created on Tue Feb 10 10:21:16 2026

@author: Shahuraj Mane
"""

n = int(input("Enter number:"))
fact = 1
for i in range(1,n + 1):
    fact = fact * i
print("Factorial:",fact)
