from django.shortcuts import render
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .filters import BookFilter
from .forms import BookForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend



class BookListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'author', 'publication_year']


    def get_queryset(self):
        title = self.kwargs['title']
        author = self.kwargs['author']
        publication_year = self.kwargs['publication_year']
        if title:
            return Book.objects.filter(title=title)
        elif author:
            return Book.objects.filter(author=author)
        elif publication_year:
            return Book.objects.filter(publication_year=publication_year)
        else:
            return Book.objects.all()


    
class BookDetail(LoginRequiredMixin, DetailView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = Book
    template_name = 'book_detail.html' 
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.filter(pk=self.kwargs['pk'])   
    

class BookCreate(LoginRequiredMixin, CreateView):
    permission_classes = [IsAuthenticated]
    model = Book
    form_class = BookForm  
    template_name = 'book_form.html' 
    success_url = reverse_lazy('book-list') 

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class BookUpdate(LoginRequiredMixin, UpdateView):
    permission_classes = [IsAuthenticated]
    model = Book
    form_class = BookForm 
    template_name = 'book_form.html' 
    success_url = reverse_lazy('book-list') 
  

        

class BookDelete(LoginRequiredMixin, DeleteView):
    permission_classes = [IsAuthenticated]
    model = Book
    template_name = 'book_confirm_delete.html'  
    success_url = reverse_lazy('book-list') 

    def perform_destroy(self, instance):
        instance.delete()

