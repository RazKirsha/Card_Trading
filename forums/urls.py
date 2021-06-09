from django.urls import path
from . import views

urlpatterns = [
    path('forum/', views.forum, name='forum'),
    path('forum/<int:pk>', views.spec_topic, name='topic'),
    path('write_topic/', views.write_topic, name='write_topic'),
    path('write_comment/<int:pk>', views.write_comment, name='write_comment'),
    path('write_topic/<int:pk>/delete', views.DeleteTopic.as_view(), name='delete_topic'),
    path('write_comment/<int:pk>/delete', views.DeleteComment.as_view(), name='delete_comment'),
]