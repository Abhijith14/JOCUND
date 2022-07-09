from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import Group

from .models import account

admin.site.register(account)

admin.site.unregister(Group)

admin.site.site_header = "PROJECT JOCUND"
