from django.shortcuts import render
from django.views.generic.detail import DetailView
from  .models import Book
from .models import Library

# Create your views here.
def list_books(request):
    book = Book.objects.all()
 
    return render(request, 'relationship_app/list_books.html', { 'book': book })


class LibraryDetailView(DetailView):
    model = Book, Library 
    template_name = 'relationship_app/library_detail.html'
    context_object_name = ['books', 'library']
    
    def get_context_data(self, **kwargs):
        """
        Add additional context data to the view.

        This method extends the context data provided by the parent class
        to include specific library details.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data dictionary with added library details.
        """
        context = super().get_context_data(**kwargs)
        context['library'] = self.get_library()  # Fetch specific library details
        return context

    def get_library(self):
        # Assuming you have a Library model and a ForeignKey from Book to Library
        library_id = self.kwargs.get('library_id')
        return Library.objects.get(id=library_id)