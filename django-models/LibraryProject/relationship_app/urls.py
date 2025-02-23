from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView
from . import views

app_name = 'relationship_app'
urlpatterns = [    
    path('lib/<int:pk>/', LibraryDetailView.as_view(), name='lib_detail'),
    path('books/', list_books, name='booklist'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

]
