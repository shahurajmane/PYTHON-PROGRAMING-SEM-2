# -*- perform basic dictionary operations add, update, and delete key-value pairs -*-
"""
Created on Tue Mar 24 10:20:26 2026

@author: Shahuraj Mane
"""

student = {}
student["name"] = "Rahul" 
student["age"] = 20 
student["course"] = "Python"
print("Dictionary after adding elements:") 
print(student)
student["age"] = 21
print("\nDictionary after updating a value:") 
print(student)
del student["course"]
print("\nDictionary after deleting a key-value pair:") 
print(student)
