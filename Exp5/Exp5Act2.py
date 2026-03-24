# -*- Find students present in both classes -*-
"""
Created on Tue Mar 24 10:49:11 2026

@author: Shahuraj Mane
"""

classA = set(map(int, input("Enter roll numbers for Class A: ").split()))
classB = set(map(int, input("Enter roll numbers for Class B: ").split()))

common_students = classA & classB

print("Students present in both classes:", common_students)
