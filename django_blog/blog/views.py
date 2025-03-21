from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm, PostForm, CommentForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/registation/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.GET.get('next', 'index')  # Redirect to previous page or index
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'blog/registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/registration/profile.html', {'form': form}) 


class ListPostView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

    def get_context_data(self, **kwargs):
        context =  super(ListPostView, self).get_context_data(**kwargs)
        return context

class DetailPostView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context =  super(DetailPostView, self).get_context_data(**kwargs)
        post = self.get_object()
        return context
    
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def create_post(request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        return render(request, 'blog/create.html', {'form': form})
    

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def update_post(request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'blog/update.html', {'form': form})
    
class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def delete_post(request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('index')
    

class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment.html'
    context_object_name = 'comments'
    ordering = ['-created_at']

    def get_queryset(self):
        self.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return Comment.objects.filter(post=self.post).order_by('-created_at')
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['post'] = self.post
        return context

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'blog/detail_comment.html'
    context_object_name = 'comment'


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/create_comment.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['post_id']})
    
    

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = Comment
   form_class = CommentForm
   template_name = 'blog/update_comment.html'

   def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
   
   def get_success_url(self):
       return reverse('post-detail', kwargs={'pk': self.kwargs['post_id']})
   

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'
    

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['post_id']})
    
