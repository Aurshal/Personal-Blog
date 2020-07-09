from django.contrib import admin
from django.urls import path, include
from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.blog_page,name = 'blog_page'),
    path('blog/<int:blog_id>/',views.blog_detail,name = 'blog_detail')
]