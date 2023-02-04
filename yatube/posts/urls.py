# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index),
    # path('group/<slug>/', views.group_posts),
    path('group/group_list.html/', views.group_posts),

]
