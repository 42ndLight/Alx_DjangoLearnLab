from bookshelf.models import Book

books = Book.objects.all()

for book in books:
    print({
        'Title': book.title,
        'Author': book.author,
        'Publication Year': book.publication_year,
    })