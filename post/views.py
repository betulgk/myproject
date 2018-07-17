from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from .forms import postForm


def home_view(request):
    return render(request, 'home.html', {})



def education_bar(request):
    return render(request, 'education.html', {})


def post_new(request):
    form = postForm()
    info = Post.objects.all()
    print ("aaaaa")
    if request.method == 'POST':

        post_name = request.POST.get('post_name')
        post_content = request.POST.get('post_content')
        post_author = User.objects.first()



        add = Post(author=post_author, post_name=post_name, post_content=post_content)
        add.save()

    return render(request, 'home.html', {'form': form})
