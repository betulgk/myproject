from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .models import Post
from django.contrib.auth.forms import *
from .forms import PostForm
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        form = PostForm()
        posts = Post.objects.all()

        return render(request, self.template_name, {'form': form, 'posts': posts})


class JsonTestView(View):
    def get(self, request, **kwargs):
        print(kwargs)
        new_msg = request.GET;
        print(new_msg)
        posts = Post.objects.filter(id__gt=int(kwargs.get('pk'))).order_by('-pub_date')[:10]

        post_lists = []

        for post in posts:
            post_lists.append({
                'id': post.id,
                'content': post.post_content,
                'name': post.post_name,
            })

        return JsonResponse(post_lists, safe=False)

    def post(self, request, *args, **kwargs):
        # form = PostForm(request.POST)

        """
            post_name = request.POST.get('post_name')
            post_content = request.POST.get('post_content')
            post_author = User.objects.first()
            add = Post(author=post_author, post_name=post_name, post_content=post_content)
            add.save()
            posts = Post.objects.all()
            args = {'form': form, 'post_name ': post_name, 'post_content': post_content, 'posts': posts}

            return render(request, 'home.html', args)"""

        print(request.POST)
        a = request.POST.get('post_content', None)
        b = request.POST.get('post_name', None)

        new_post = Post(author='', post_name=b, post_content=a)

        new_post.save()

        return JsonResponse({'saved': 'True'})
