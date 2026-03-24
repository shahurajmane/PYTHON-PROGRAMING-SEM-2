# -*- Count frequency of items purchased by customers -*-
"""
Created on Tue Mar 24 11:02:37 2026

@author: Shahuraj Mane
"""

items = input("Enter purchased items separated by space: ").split()

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Item Frequency:")
for item, count in frequency.items():
    print(item, ":", count)
