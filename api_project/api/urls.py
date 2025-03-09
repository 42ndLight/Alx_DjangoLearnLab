from django.urls import include, path
from .views import BookList
from rest_framework import routers
from .views import BookViewSet



router = routers.DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)), 
]