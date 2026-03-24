# -*- A libarary dictionary stores book name and price. update book price -*-
"""
Created on Tue Mar 24 10:33:42 2026

@author: Shahuraj Mane
"""

library = {
    "Python Basics": 250,
    "Data Science": 400,
    "Machine Learning": 500
}

print("Available books and prices:")
for book, price in library.items():
    print(book, ":", price)

book_name = input("Enter the book name to update price: ")

if book_name in library:
    new_price = float(input("Enter new price: "))
    library[book_name] = new_price
    print("Price updated successfully!")
else:
    print("Book not found!")

print("Updated library:")
for book, price in library.items():
    print(book, ":", price)
