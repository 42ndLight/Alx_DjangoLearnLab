from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.db.models import Q
from .forms import ExampleForm

# Create your views here.
def index(request):
    if request.user.has_perm('bookshelf.can_view_book'):
        return render(request, 'bookshelf/index.html', {'user': request.user})
    else:
        return render(request, 'bookshelf/permission_denied.html') 

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ExampleForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def book_search(request):
    query = request.GET.get('q', '').strip()

    if not query:
        return render(request, 'bookshelf/book_list.html', {'books': []})
    

    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

    
    return render(request, 'bookshelf/form_example.html', {'books': books})