# Check leap year
"""
Created on Tue Feb 10 09:54:54 2026

@author: Shahuraj Mane
"""

n = int(input("Enter number of rows: ")) 

for i in range(1, n + 1):
  for j in range(1, i + 1): 
    print(j, end=" ")
  print()
