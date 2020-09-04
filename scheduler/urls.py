from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
  path('user/<int:pk>/task/<str:day>/', views.task_scheduler_view, name='user_home'),
  path('', views.sign_in, name='login'),
  path('register/', views.sign_up, name="register"),
  path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
