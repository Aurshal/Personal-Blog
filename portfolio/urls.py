from django.contrib import admin
from django.urls import path, include
from portfolio import views

app_name = 'potfolio'

urlpatterns = [
    path('',views.homepage,name = 'Homepage'),
    
         ]
