from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return(redirect("profile"))
        else:
            print("error", form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})


def profile(request):
    return render(request, 'registration/profile.html')

