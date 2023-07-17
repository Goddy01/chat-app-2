from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.home_chat, name='index'),
    path('directs/<str:username>/', views.direct_messages, name='direct_messages'),
    path('send/', views.send_direct, name='send-direct'),
]