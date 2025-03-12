from django.db import models

# The Author model represents an author with a name.
class Author(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

# The Book model represents a book with a title, publication year, and a foreign key to the Author model.
# The foreign key establishes a many-to-one relationship between Book and Author, meaning each book is associated with one author,
# but an author can have multiple books.
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title, self.publication_year, self.author
