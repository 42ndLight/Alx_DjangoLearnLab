from django.urls import path
from .views import list_books, LibraryDetailView

app_name = 'relationship_app'
urlpatterns = [    
    path('lib/<int:pk>/', LibraryDetailView.as_view(), name='lib_detail'),
    path('books/', list_books, name='booklist'),
]
