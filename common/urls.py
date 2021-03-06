from django.urls import path
from django.contrib.auth import views as auth_views
from common.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
]
