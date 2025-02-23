from django.urls import path
from .views import booklist, BookDetailView

app_name = 'relationship_app'
urlpatterns = [    
    path('lib/<int:pk>/', BookDetailView.as_view(), name='lib_detail'),
    path('books/', booklist, name='booklist'),
]
