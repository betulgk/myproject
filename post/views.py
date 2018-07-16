from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import post
from .forms import postForm



def home_view(request):
    return render(request, 'home.html', {})


def education_bar(request):
    return render(request, 'education.html', {})

def post_new(request):
    form = postForm()
    veri = post.models.objects.all()

    if (request.method=='POST'):

        postName= request.POST['post_name']
        postContent = request.POST['post_content']

        ekle = post.models(post_name=postName, post_content=postContent)

        ekle.save()

        return render(request, 'home.html', {'form': form})