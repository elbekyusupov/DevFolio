from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('products', views.ProductPage.as_view(), name='products'),
    path('login', views.LoginPage.as_view(), name='login'),
    path('profile', views.ProfilePage.as_view(), name='profile'),
    path('logout', views.LogoutPage.as_view(), name='logout'),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('blog/<int:id>', views.BlogPage.as_view(), name='blog'),
    path('reply/<int:id>', views.ReplyPage.as_view(), name='reply'),
    path('edit_comment/<int:id>', views.CommentPage.as_view(), name='edit_comment'),
    path('delete_comment/<int:id>', views.DeleteCommentPage.as_view(), name='delete_comment'),

    path('api/v1/', include('ourblog.api.urls')),
]