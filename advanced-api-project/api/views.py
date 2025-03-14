from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from .filters import BookFilter
from .forms import BookForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class BookList(LoginRequiredMixin, FilterView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = Book
    template_name = 'book_list.html'  
    context_object_name = 'books'
    filterset_class = BookFilter 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                title__icontains=search_query
            ) | queryset.filter(
                author__name__icontains=search_query
            ) | queryset.filter(
                publication_year__icontains=search_query
            )
        # Add ordering
        ordering = self.request.GET.get('ordering')
        if ordering in ['title', 'publication_year']:
            queryset = queryset.order_by(ordering)
        return queryset


    
class BookDetail(LoginRequiredMixin, DetailView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = Book
    template_name = 'book_detail.html' 
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.filter(pk=self.kwargs['pk'])   
    

class BookCreate(LoginRequiredMixin, CreateView):
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
    model = Book
    form_class = BookForm 
    template_name = 'book_form.html' 
    success_url = reverse_lazy('book-list') 
  

        

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'  
    success_url = reverse_lazy('book-list') 

    def perform_destroy(self, instance):
        instance.delete()

