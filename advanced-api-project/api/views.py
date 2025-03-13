from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response

# Create your views here.
class BookList(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def book_list(request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def book_detail(request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
class BookCreate(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'pages', 'price']

    def book_create(request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BookUpdate(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'pages', 'price']

    def book_update(request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BookDelete(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = '/'

    def book_delete(request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response('Book deleted successfully')

