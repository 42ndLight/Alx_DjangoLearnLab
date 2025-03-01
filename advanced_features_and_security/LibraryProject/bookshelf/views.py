from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required
from .models import Book
from bookshelf.forms import BookForm

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
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})