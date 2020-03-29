from django.urls import path,include
from django.contrib.auth import views as auth_views
from .import views


urlpatterns=[
path('signup',views.signup,name='signup'),
path('login',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
path('logout',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
path('profile',views.profile,name='profile'),
path('profile_view',views.profile_view,name='profile_view'),

path('change_password',views.change_password,name='change_password')



]