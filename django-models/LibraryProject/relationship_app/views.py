from django.shortcuts import render
from django.views.generic import ListView
from  .models import Book

# Create your views here.
def booklist(request):
    book = Book.objects.all()
    context = {
        'book': book
    }
    return render(request, 'relationship_app/list_books.html', context)


class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/lib_detail.html'
    context_object_name = 'book'
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Fetch all books in the library
        return context
    