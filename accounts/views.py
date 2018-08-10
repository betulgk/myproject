from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):  # signup here
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/accounts/login')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})


def logout(request):  # logout here
    logout(request)
    return redirect("http://127.0.0.1:8000/home")
