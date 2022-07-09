from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import acc_form
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.


def login_view(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('/dashboard/')

    if request.method == "POST":
        user = request.POST.get('username')
        password = request.POST.get('password')

        form = acc_form(request.POST)
        if user != '' and user is not None:
            if password != '' and password is not None:
                if form.is_valid():
                    acc = authenticate(username=user, password=password)
                    if acc:
                        login(request, acc)
                        return redirect('/dashboard/')
                else:
                    messages.warning(request, "Invalid Username and password")
            else:
                messages.warning(request, "enter your password")
        else:
            messages.warning(request, "enter your username")
    else:
        form = acc_form()

    context['login_form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')


def test(request):
    print(request.GET['pass'])
    hashed_pass = make_password(request.GET['pass'])
    return HttpResponse(hashed_pass)
