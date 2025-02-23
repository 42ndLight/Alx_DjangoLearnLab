from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from  .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def list_books(request):
    book = Book.objects.all()
 
    return render(request, 'relationship_app/list_books.html', { 'book': book })


class LibraryDetailView(DetailView):
    model = Book, Library 
    template_name = 'relationship_app/library_detail.html'
    context_object_name = ['books', 'library']
    
    def get_context_data(self, **kwargs):
        """
        Add additional context data to the view.

        This method extends the context data provided by the parent class
        to include specific library details.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data dictionary with added library details.
        """
        context = super().get_context_data(**kwargs)
        context['library'] = self.get_library()  # Fetch specific library details
        return context

    def get_library(self):
        # Assuming you have a Library model and a ForeignKey from Book to Library
        library_id = self.kwargs.get('library_id')
        return Library.objects.get(id=library_id)
    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to home or dashboard page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User Login View
class LoginView(LoginView):
    template_name = 'relationship_app/login.html'

# User Logout View
class LogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to login page after logout


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')