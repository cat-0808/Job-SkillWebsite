"""
URL configuration for AdminBase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AdminHome import views
from AdminHome.views import CustomLoginView
from django.contrib.auth.views import LoginView, LogoutView
from AdminHome.views import home, create_job_post, create_skill_exchange

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('create-job/', views.create_job_post, name='create_job'),
    path('create-skill/', views.create_skill_exchange, name='create_skill'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
