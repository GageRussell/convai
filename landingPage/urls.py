from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('email', views.email, name='email'),
    path('chat', views.chat, name='chat'),
    path('<str:room_name>/', views.room, name='room')
]