from django.urls import path

from blog.views import BlogList, BlogDetail, BlogCreate, BlogUpdate, BlogDelete

urlpatterns = [
    path('', BlogList.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetail.as_view(), name='post_detail'),
    path('post/new/', BlogCreate.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdate.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDelete.as_view(), name='post_delete'),
]