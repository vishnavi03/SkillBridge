from django.urls import path
from accounts import views

urlpatterns = [

    path('', views.home, name='home'),

    path('signup/', views.signup, name='signup'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('profile/', views.profile, name='profile'),

    path('dashboard/', views.dashboard, name='dashboard'),

    # 🌍 public profile
    path(
        'user/<str:username>/',
        views.public_profile,
        name='public_profile'
    ),

]