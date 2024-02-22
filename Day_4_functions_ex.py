library = [
    {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
    {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
    {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False},
]


# Task 1: Create a function add_book(library, new_book) that adds book to the library

def add_book(library, new_book):
  library.append(new_book) # Here we passing 
  return library
  
new_book = {"title": "Algorithms", "author": " Robert Sedgewick", "year": 2013, "available": True}

#Pass by value: Creates a copy and updates that copy
new_library = add_book(library.copy(), new_book)

# Pass by reference: Updates the original library
print(library)

print()

#Task 2: search_by_author(library, author_name): Returns a library with only books by that author
def search_by_author(library, author_name):
  author_books = []
  for book in library:
    if book["author"] == author_name:
      author_books.append(book)
  return author_books
print(search_by_author(library, "Mark Lutz"))

print()

# List comprehension
def search_by_author_new(library, author_name):
  author_books = [book for book in library if book["author"] == author_name]
  return author_books
print(search_by_author_new(library, "Mark Lutz"))


print()
# Task 3: check_out_book(library, title) marks a books as not available if it exists and available in the library
def check_out_book(library, title):
  for book in library:
    if book["title"] == title and book["available"] == True:
      book["available"] = False
      return "Book checked out successfully"
  return "Book is not available"
print(check_out_book(library, "Fluent Python"))

