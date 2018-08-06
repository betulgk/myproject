from django.shortcuts import render, redirect, render_to_response

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login_view(request):

    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('http://127.0.0.1:8000/home')
    else:
        form = AuthenticationForm()
    return render(request, '/home/betul/Desktop/myproject/post/templates/login.html', {'form': form })





