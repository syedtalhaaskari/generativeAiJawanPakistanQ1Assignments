"""
Write a for loop to assign book stock categories based on the number of copies available:
Copies >= 5: "Popular"
Copies >= 3 and < 5: "Available"
Copies < 3: "Limited"
Store these stock categories in a same dict i.e library_books.
"""

import pprint

print("Problem No. 4")

library_books = {
    "The Great Gatsby": 4,
    "1984": 6,
    "To Kill a Mockingbird": 3,
    "The Catcher in the Rye": 5,
    "Moby Dick": 2,
}

print("\nLibrary Books Dictionary:", library_books, end="\n\n")

for name, copies in library_books.items():
    category = ""
    if copies >= 5:
        category = "Popular"
    elif copies >= 3 and copies < 5:
        category = "Available"
    elif copies < 3:
        category = "Limited"
    library_books[name] = { "copies": copies }
    library_books[name]["category"] = category

print("\nAfter assigning category")
pprint.pprint(library_books)
