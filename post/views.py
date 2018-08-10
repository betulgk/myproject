from django.shortcuts import render
from django.views import View
from .models import Post
from django.http import JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class HomeView(View):
    template_name = 'home.html'

    def post(self,request):

        return HttpResponseRedirect('/')

    def get(self, request):
         # form = PostForm()
         # posts = Post.objects.all().order_by('-pub_date')

        post_list = Post.objects.all().order_by('-pub_date')
        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, 2)


        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'posts': posts})

    # def index(request):
    #     post_list = Post.objects.all()
    #     page = request.GET.get('page',1)
    #     paginator = Paginator(post_list,10)
    #
    #     try:
    #         posts = paginator.page(page)
    #     except PageNotAnInteger:
    #         posts = paginator.page(1)
    #     except EmptyPage:
    #         posts = paginator.page(paginator.num_pages)
    #
    #     return render(request, 'home.html', {'posts': posts})


class LoginHomeView(View):
    template_name = 'login-home.html'

    def get(self, request):
        # form = PostForm()
        # posts = Post.objects.all().order_by('-pub_date')

        post_list = Post.objects.all().order_by('-pub_date')
        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, 2)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request, 'login-home.html', {'posts': posts})

    def index(request):
        post_list = Post.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, 10)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request, 'login-home.html', {'posts': posts})


class JsonTestView(View):

    def get(self, request, **kwargs):

        new_msg = request.GET;
        print(new_msg)
        posts = Post.objects.filter(id__gt=int(kwargs.get('pk'))).order_by('-pub_date')

        post_lists = []

        for post in posts:
            post_lists.append({
                'id': post.id,
                'content': post.post_content,
                'name': post.post_name,
            })

        return JsonResponse(post_lists, safe=False)

    def post(self, request, *args, **kwargs):

        a = request.POST.get('post_content', None)
        b = request.POST.get('post_name', None)

        new_post = Post(author='', post_name=b, post_content=a)

        new_post.save()

        return JsonResponse({'saved': 'True'})
