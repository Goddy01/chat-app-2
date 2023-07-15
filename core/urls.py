from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('directs/<str:username>/', views.direct_messages, name='direct_messages'),
]