# -*- find the union and intersection of two sets -*-
"""
Created on Tue Mar 24 10:27:45 2026

@author: Shahuraj Mane
"""

set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))
union_set = set1 | set2 # or set1.union(set2)
intersection_set = set1 & set2 # or set1.intersection(set2)
print("Union of the sets:", union_set) 
print("Intersection of the sets:", intersection_set)
