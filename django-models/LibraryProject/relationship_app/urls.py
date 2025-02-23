from django.urls import path
from .views import booklist, BookListView

app_name = 'relationship_app'
urlpatterns = [    
    path('lib/<int:pk>/', BookListView.as_view(), name='lib_detail'),
    path('books/', booklist, name='booklist'),
]
