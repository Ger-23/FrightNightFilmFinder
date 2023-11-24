from . import views
from django.urls import path
from .views import TeamMemberDetails

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', TeamMemberDetails.as_view(), name='about'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
