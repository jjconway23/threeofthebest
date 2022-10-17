from django.urls import path
from . import views
urlpatterns = [
    path('', views.ListHomeView.as_view(), name='home'),
    path('reviews/<int:pk>', views.DetailPostView.as_view(), name='post-details'),
    path('add_post/', views.CreatePostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', views.DeletePostView.as_view(), name='delete_post'),
]