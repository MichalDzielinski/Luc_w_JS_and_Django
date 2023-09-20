from django.urls import path
from . import views

app_name= 'posts'
urlpatterns = [
    path('', views.post_list_and_create, name='main-board'),
    path('like-unlike/', views.like_unlike_post, name='like-unlike'),
    path('<pk>/', views.post_detail, name='post-detail'),
    path('data/<int:num_posts>/', views.load_post_data_view, name='posts-data'),
    path('<pk>/data/', views.post_detail_data_view, name='post-detail-data'),
]

    