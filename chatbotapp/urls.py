
from django.urls import path
from . import views

app_name = 'chatbotapp'

urlpatterns = [
    path('chatbot', views.chatbot, name='chatbot'),  # chatbot 뷰 함수와 연결
]