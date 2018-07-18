from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import View

from .models import Post
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *
from .forms import postForm


class HomeWiew(View):

    template_name = 'home.html'

    def get(self, request):
        form = postForm()

        return render(request, 'home.html', {'form': form})

    def post(self, request):

        form = postForm()

        if request.method == 'POST':
            post_name = request.POST.get('post_name')
            post_content = request.POST.get('post_content')
            post_author = User.objects.first()

            add = Post(author=post_author, post_name=post_name, post_content=post_content)
            add.save()

            args = {'form': form , 'post_name ': post_name, 'post_content': post_content }
        return render(request, 'home.html', args )


    




class EducationView(View):

    template_name = 'education.html'

    def education_bar(self,request):
        return render(request, 'education.html', {})


""""
def home_view(request):
    return render(request, 'home.html', {})




def education_bar(request):
    return render(request, 'education.html', {})




#is_valid () , class base view,
def post_new(request):
    form = postForm()
    info = Post.objects.all()
    if request.method == 'POST':

        post_name = request.POST.get('post_name')
        post_content = request.POST.get('post_content')
        post_author = User.objects.first()

        add = Post(author=post_author, post_name=post_name, post_content=post_content)
        add.save()

    return render(request, 'home.html', {'form': form})


def login(request):



    form = AuthenticationForm
    if (request.method == 'POST'):
        username = request.method['username']
        password = request.method['password']
        login_control= AuthenticationForm(data=request.POST)
        if (login_control.is_valid()):
            user = authenticate(username=username, password=password)
            login(request, user)

    return render(request, 'login.html', locals())


def information(request):
    read = request.user.id
    if(not information):
        return HttpResponseRedirect('/')
    return render(request,'infromation.html',locals())


def logout(request):
    read = request.user.id
    if(not read):
        return HttpResponseRedirect('/')
    logout(request)
    return HttpResponse('Çıkış Yapıldı!, Lütfen Sayfayı Yenileyin!')
    
"""