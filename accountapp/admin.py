from django.contrib import admin

# Register your models here.
from django.contrib import admin
from accountapp.models import HelloWorld

admin.site.register(HelloWorld)