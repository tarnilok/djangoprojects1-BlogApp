from django.urls import path
from .views import navbar, user_register, user_login, user_logout, about_page, create_post, user_profile, home_page, user_update, detail_post, delete_post, edit_post, post_comments, post_like

urlpatterns = [
    path('', home_page, name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('about/', about_page, name='about'),
    path('profile/<int:id>/', user_profile, name='profile'),
    path('update/<int:id>/', user_update, name='update'),
    path('newpost/', create_post, name='newpost'),
    path('detail/<int:id>', detail_post, name='detail'),
    path('delete/<int:id>', delete_post, name='delete'),
    path('postedit/<int:id>', edit_post, name='postedit'),
    path('comments/', post_comments, name='comments'),
    path('like/', post_like, name='like'),
]