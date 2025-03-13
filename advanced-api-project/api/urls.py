from django.contrib import admin
from django.urls import path, include
from api.views import BookListView, BookDetailView

urlpatterns = [
    path('/books/', BookListView.as_view(), name='book-list'),
    path('/books/', BookListView.as_view(), name='book-create'),
    path('/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('admin/', admin.site.urls),
]