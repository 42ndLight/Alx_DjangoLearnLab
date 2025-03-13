from django.contrib import admin
from django.urls import path, include
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete


urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('books/create/', BookCreate.as_view(), name='book_create'),
    path('books/update/<int:pk>/', BookUpdate.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDelete.as_view(), name='book_delete'),
    path('admin/', admin.site.urls, name='admin'),
]