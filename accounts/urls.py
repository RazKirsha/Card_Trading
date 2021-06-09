from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    # path('search/', views.homepage, name='homepage'),
    path('search/', views.Homepage.as_view(), name='homepage'),
    path('profile/', views.user_profile, name='profile'),
    path('change_status/<int:pk>', views.change_status, name='change_status'),
]