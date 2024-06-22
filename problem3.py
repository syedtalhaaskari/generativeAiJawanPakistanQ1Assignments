"""
Create a dictionary named library_books with the following key-value pairs:
"The Great Gatsby": 4
"1984": 6
"To Kill a Mockingbird": 3
"The Catcher in the Rye": 5
"Moby Dick": 2

1. Write a for loop with range to add 2 more copies to each book. Update the dictionary accordingly.
2. Write a for loop to calculate the total number of books in the library. Print the total count.
"""

print("Problem No. 3")

library_books = {
    "The Great Gatsby": 4,
    "1984": 6,
    "To Kill a Mockingbird": 3,
    "The Catcher in the Rye": 5,
    "Moby Dick": 2,
}

print("\nLibrary Books Dictionary:", library_books, end="\n\n")

total_books = 0

for key in library_books.keys():
    library_books[key] += 2
    total_books += library_books[key]

print("Total Books in Library:", total_books)
