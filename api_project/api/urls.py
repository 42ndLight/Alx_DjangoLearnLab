from django.urls import include, path
from .views import BookList
from rest_framework import routers
from .views import BookViewSet
from rest_framework.authtoken import views



router = routers.DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token) 
]