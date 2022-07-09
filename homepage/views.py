from django.shortcuts import render, redirect

# Create your views here.

def homepage(request):

    if request.user.is_authenticated:
        return redirect('/dashboard/')

    return render(request, 'homepage.html', {})

