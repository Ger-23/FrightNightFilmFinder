from . import views
from django.urls import path
from .views import TeamMemberDetails

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', TeamMemberDetails.as_view(), name='about'),
    path('add/', views.post_add, name='post_add'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('<slug:slug>/delete/', views.post_delete, name='post_delete'),
]

handler403 = "FNFFapp.views.handler403"
handler404 = "FNFFapp.views.handler404"
handler405 = "FNFFapp.views.handler405"
handler500 = "FNFFapp.views.handler500"