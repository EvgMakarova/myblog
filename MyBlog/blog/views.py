from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .forms import PostForm

class PostView(View):
    # Вывод записей
    def get(self, request): #наследуется от View
        posts = Post.objects.all()[::-1]
        context = {
            'post_list': posts,
            'name': 'Главная страница'
        }
        return render(request, 'blog/blog.html', context)
    def indexX(request):
        context ={
            'name': 'imya'
        }
        return render(request, 'blog/post.html',context)
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