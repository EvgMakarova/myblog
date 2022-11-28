from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

class PostView(View):
    # Вывод записей
    def get(self, request): #наследуется от View
        posts = Post.objects.all()[::-1]
        context = {
            'post_list': posts,
            'name': 'Главная страница',
        }
        return render(request, 'blog/blog.html', context)

    def add(request):
        if request.method =="POST":
            form = PostForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                newPost = Post.objects.create(title=cd['title'],descriptions=cd['descriptions'],author=cd['author'],date=cd['date'], )
                newPost.save()
                return redirect('/')
        else:
            form = PostForm()

        context = {
            'name': 'Добавление нового поста',
            'form': form
        }
        return render(request, 'blog/add.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_obj_name = 'post'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/add.html'
    fields = ['title', 'descriptions', 'author', 'date']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url= '/'