from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('create/', views.create_article, name='create_article'),
]
