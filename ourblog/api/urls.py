from django.urls import path
from . import views

urlpatterns = [
    path('comments', views.CommentView.as_view(), name='comments_list'),
    path('comments-create', views.CommentCreateView.as_view(), name='comments_create'),
    path('comments-list-create', views.CommentListCreateView.as_view(), name='comments_list_create'),
    path('comments-retrieve/<int:pk>', views.CommentRetrieveView.as_view(), name='comments_retrieve'),
    path('comments-update/<int:pk>', views.CommentUpdateView.as_view(), name='comments_update'),
    path('comments-retrieve-update/<int:pk>', views.CommentRetrieveUpdateView.as_view(), name='comments_retrieve_update'),
    path('comments-delete/<int:pk>', views.CommentDestroyView.as_view(), name='comments_delete'),
    path('comments-retrieve-delete/<int:pk>', views.CommentRetrieveDestroyView.as_view(), name='comments_retrieve_delete'),
    path('comments-retrieve-update-delete/<int:pk>', views.CommentRetrieveUpdateDestroyView.as_view(), name='comments_retrieve_update_delete'),
    path('blogs', views.BlogsView.as_view(), name='blogs_list'),
    path('replys', views.ReplysView.as_view(), name='replys_list'),
    path('cats', views.CatsView.as_view(), name='cats_list'),
]