from django.urls import path
from .views import navbar, user_register, user_login, user_logout, about_page, create_post, user_profile, home_page, user_update, detail_post, delete_post, edit_post

urlpatterns = [
    path('', home_page, name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('about/', about_page, name='about'),
    path('profile/<str:slug>', user_profile, name='profile'),
    path('update/<str:slug>', user_update, name='update'),
    path('newpost/', create_post, name='newpost'),
    path('detail/<str:slug>', detail_post, name='detail'),
    path('delete/<str:slug>', delete_post, name='delete'),
    path('postedit/<str:slug>', edit_post, name='postedit'),
]