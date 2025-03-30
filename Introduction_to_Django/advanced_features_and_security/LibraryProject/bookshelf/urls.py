from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/edit/', views.edit_book, name='book_edit'),
    path('books/search/', views.book_search, name='book_search'),
]