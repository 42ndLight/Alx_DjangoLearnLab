from bookshelf.models import Book

books = Book.objects.get(title='1984')

print({
    'Title': book.title,
    'Author': bookauthor,
    'Publication Year': book.publication_year,
    })