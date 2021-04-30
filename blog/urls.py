from django.urls import path
from .views import BlogUpdateView, BlogDeleteView, blog_register, blog_login, blog_logout, blog_list_view, blog_detail_view, blog_create_view
# modules to reset password
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('logout', blog_logout, name='blog_logout'),
    path('login/', blog_login, name='blog_login'),
    path('register/', blog_register, name='blog_register'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', blog_create_view, name='post_new'),

    path('post/<int:my_id>/', blog_detail_view, name='post_detail'),
    
    path('', blog_list_view, name='home'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
