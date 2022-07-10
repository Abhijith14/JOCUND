"""JOCUND URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from homepage.views import homepage
from authentication.views import login_view, logout_view, test
from dashboard.views import dash_view
from transaction.views import transaction_view, request_view
from jclass.views import jclass_view, jclass_launch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dash_view, name='dashboard'),
    path('transaction/', transaction_view, name='transaction'),
    path('request/', request_view, name='request'),
    path('jclass/', jclass_view, name='jclass'),
    path('jclassL/', jclass_launch, name='jclassL'),
    path('test/', test, name='test'),
]
