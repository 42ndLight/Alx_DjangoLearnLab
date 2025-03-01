# LibraryProject

This project is a simple library management system built using Django. It allows users to manage books, authors, and borrowers. The system provides functionalities to add, update, delete, and view records of books and authors. Additionally, it supports borrowing and returning books, tracking the status of each book in the library.

# LibraryProject Permissions and Groups Setup

## Permissions

The following custom permissions are used in the application:

- `can_view_book`: Allows users to view the book index page.
- `can_edit_book`: Allows users to edit book details.
- `can_view`: Allows users to view the list of books.

## Groups

The following groups are used to manage permissions:

- `Librarians`: Users in this group have the `can_edit_book` permission.
- `Members`: Users in this group have the `can_view_book` and `can_view` permissions.
- `Admins`: Users in this group have all permissions, including `can_edit_book`, `can_view_book`, and `can_view`.


## Setting Up Permissions and Groups

1. **Create Permissions**:
   Add the custom permissions to the `Book` model in `models.py`:

   ```python
   from django.db import models
   from django.contrib.auth.models import AbstractUser

   class Book(models.Model):
       title = models.CharField(max_length=200)
       author = models.CharField(max_length=200)
       published_date = models.DateField()
       isbn = models.CharField(max_length=13, unique=True)
       summary = models.TextField()

       class Meta:
           permissions = [
               ('can_view_book', 'Can view book'),
               ('can_edit_book', 'Can edit book'),
               ('can_view', 'Can view book list'),
           ]
   

