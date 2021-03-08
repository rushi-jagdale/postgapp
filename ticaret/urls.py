from django.urls import path

from ticaret import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    
]
