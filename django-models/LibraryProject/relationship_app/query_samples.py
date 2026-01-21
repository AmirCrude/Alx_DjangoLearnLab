from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = author.books.all()

print("Books by author:")
for book in books_by_author:
    print(book.title)


# 2. List all books in a library
library = Library.objects.get(name="Central Library")
library_books = library.books.all()

print("\nBooks in library:")
for book in library_books:
    print(book.title)


# 3. Retrieve the librarian for a library
librarian = library.librarian
print("\nLibrarian of the library:")
print(librarian.name)
