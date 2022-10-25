from django.urls import path

from theblog.models import Category
from . import views
urlpatterns = [
    path('', views.ListHomeView.as_view(), name='home'),
    path('reviews/<int:pk>/', views.DetailPostView.as_view(), name='post-details'),
    path('add_post/', views.CreatePostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove/', views.DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/',views.ListCategoryView, name='category'),
    path('sub-category/<slug:slug>/',views.ListAllSubCategoriesView, name='sub_category'),
    path('category-list/', views.ListAllCategoriesView, name='category_list'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
    path('article/<int:pk>/add_comment/', views.CreateCommentView.as_view(), name='add_comment'),
    

    
]
