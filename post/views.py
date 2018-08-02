from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm
from django.http import JsonResponse

POST_COUNT_PER_LOAD = 1
CURRENT_POST_COUNT = 3

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        form = PostForm()
        posts = Post.objects.all().order_by('-pub_date')[:CURRENT_POST_COUNT]

        return render(request, self.template_name, {'form': form, 'posts': posts})


class JsonTestView(View):

    def get(self, request, **kwargs):

        new_msg = request.GET;
        print(new_msg)
        posts = Post.objects.all().order_by('-pub_date')[CURRENT_POST_COUNT:CURRENT_POST_COUNT+POST_COUNT_PER_LOAD]

        post_lists = []

        for post in posts:
            post_lists.append({
                'id': post.id,
                'content': post.post_content,
                'name': post.post_name,
            })

        return JsonResponse({'new_posts': post_lists}, safe=False)

    def post(self, request, *args, **kwargs):

        post_content = request.POST.get('post_content', None)
        post_name = request.POST.get('post_name', None)

        new_post = Post(author='', post_name=post_name, post_content=post_content)

        new_post.save()

        CURRENT_POST_COUNT += 1
        return JsonResponse({'saved': 'True'})


