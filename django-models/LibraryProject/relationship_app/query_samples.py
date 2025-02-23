from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author):
    books = Book.objects.filter(author=author)
    return books

# List all books in a library.
def get_books_in_library(library):
      library = Library.objects.get(name=library)
      return library.books.all()
    
         

# Retrieve the librarian for a library
def get_librarian(library):    
    library = Library.objects.get(name=library)
    return library.librarian
    