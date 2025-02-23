from django.shortcuts import render
from django.views.generic import ListView
from  .models import Book, Library

# Create your views here.
def booklist(request):
    book = Book.objects.all()
    context = {
        'book': book
    }
    return render(request, 'relationship_app/list_books.html', context)


class BookListView(ListView):
    model = Book, Library 
    template_name = 'relationship_app/library_detail.html'
    context_object_name = ['books', 'library']
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library'] = self.get_library()  # Fetch specific library details
        return context

    def get_library(self):
        # Assuming you have a Library model and a ForeignKey from Book to Library
        library_id = self.kwargs.get('library_id')
        return Library.objects.get(id=library_id)