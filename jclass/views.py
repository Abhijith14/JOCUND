from django.shortcuts import render
from jclass.CVM.main import detection_start

# Create your views here.

def jclass_view(request):
    return render(request, 'jclass.html', {})


def jclass_launch(request):
    detection_start()
    return render(request, 'jclass.html', {})

