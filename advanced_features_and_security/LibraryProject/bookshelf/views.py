from django.shortcuts import render

# Create your views here.
def index(request):
    if request.user.has_perm('bookshelf.can_view_book'):
        return render(request, 'bookshelf/index.html', {'user': request.user})
    else:
        return render(request, 'bookshelf/permission_denied.html') 

