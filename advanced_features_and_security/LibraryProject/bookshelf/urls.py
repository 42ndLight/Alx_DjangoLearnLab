from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books/<int:id>/edit/', views.book_edit, name='book_edit'),  # New URL pattern for editing a book
    path('books/search/', views.book_search, name='book_search'),
    path('permission-denied/', views.permission_denied, name='permission_denied'),
]