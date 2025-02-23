from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ("title", "author", "publication_year")

    # Enable search functionality on title and author
    search_fields = ("title", "author")

    # Add filtering options for genre and publication date
    list_filter = ("title", "publication_year")

# Register the model with the customized admin settings
admin.site.register(Book, BookAdmin)
