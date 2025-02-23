from django.urls import path
from .views import list_books, LibraryDetailView, RegisterView , UserLoginView, UserLogoutView

app_name = 'relationship_app'
urlpatterns = [    
    path('lib/<int:pk>/', LibraryDetailView.as_view(), name='lib_detail'),
    path('books/', list_books, name='booklist'),
    path("signup/", RegisterView.as_view(), name="signup"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

]
