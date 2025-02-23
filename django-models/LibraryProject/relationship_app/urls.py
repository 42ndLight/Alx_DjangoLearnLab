from django.urls import path
from .views import list_books, LibraryDetailView, RegisterView , LoginView, LogoutView

app_name = 'relationship_app'
urlpatterns = [    
    path('lib/<int:pk>/', LibraryDetailView.as_view(), name='lib_detail'),
    path('books/', list_books, name='booklist'),
    path("signup/", RegisterView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
