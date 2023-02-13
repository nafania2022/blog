from django.urls import path

from .views import *

urlpatterns = [
       path('', index, name='home'),
       path('post/<int:id_post>', post, name='post'),
       path('create/', create, name='create'),
]


