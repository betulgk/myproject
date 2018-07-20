from django.shortcuts import render
from django.views import View
from .models import Post
from django.contrib.auth.forms import *
from .forms import PostForm


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        form = PostForm()
        posts = Post.objects.all()

        """post_name = posts.post_name
        post_author = posts.author
        post_content = posts.post_content"""
        return render(request, self.template_name, {'form': form, 'posts':posts})

    def post(self, request):
        form = PostForm(request.POST)

        if request.method == 'POST':
            post_name = request.POST.get('post_name')
            post_content = request.POST.get('post_content')
            post_author = User.objects.first()

            add = Post(author=post_author, post_name=post_name, post_content=post_content)
            add.save()

            args = {'form': form, 'post_name ': post_name, 'post_content': post_content}
        return render(request, 'home.html', args)


def education_bar(request):
    return render(request, 'education.html', {})

