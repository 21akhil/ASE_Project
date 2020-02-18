from django.conf.urls import url
from sign_up import views
from django.urls import path
urlPatterns = [
    path('',views.base,name = "index"),
]