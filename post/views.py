from django.core.serializers import json
from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Post
from django.contrib.auth.forms import *
from .forms import PostForm
from django.http import JsonResponse


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        form = PostForm()
        posts = Post.objects.all()

        return render(request, self.template_name, {'form': form, 'posts': posts})

    def post(self, request):
        form = PostForm(request.POST)

        if request.method == 'POST':
            post_name = request.POST.get('post_name')
            post_content = request.POST.get('post_content')
            post_author = User.objects.first()
            add = Post(author=post_author, post_name=post_name, post_content=post_content)
            add.save()
            posts = Post.objects.all()
            args = {'form': form, 'post_name ': post_name, 'post_content': post_content, 'posts': posts}

        return render(request, 'home.html', args)


class JsonTestView(View):
    def get(self, request):
        posts = Post.objects.all()

        post_lists = []

        for post in posts:
            post_lists.append({
                'id': post.id,
                'content': post.post_content,
                'name': post.post_name,
            })

        data = {
            'posts': post_lists
        }

        args = {'posts': posts, 'data': data}

        return render(request, 'home.html', args)
