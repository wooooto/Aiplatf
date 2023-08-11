from django.urls import path
from . import views

app_name = 'askapp'

urlpatterns = [
    path('write/', views.askwrite, name='askwrite'),
    path('list/', views.asklist, name='asklist'),
    # Add more URLs as needed
]
