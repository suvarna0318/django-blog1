from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreatView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(),name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post_detail'),
    path('post/new/', PostCreatView.as_view(),name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name='post_delete'),
    
    path('about/', views.about,name='about'),


]