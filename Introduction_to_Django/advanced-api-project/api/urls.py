from django.contrib import admin
from .views import BookCreate, BookDetail, BookListView, BookUpdate, BookDelete
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register(r'books', BookListView)



urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('books/create/', BookCreate.as_view(), name='book_create'),
    path('books/update/<int:pk>/', BookUpdate.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDelete.as_view(), name='book_delete'),
    path('admin_api/', admin.site.urls, name='admin_api'),
]