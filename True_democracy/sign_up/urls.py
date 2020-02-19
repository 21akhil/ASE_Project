from django.conf.urls import url
from sign_up import views
from django.urls import path

app_name = 'sign_up'

urlpatterns = [
	path('',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]