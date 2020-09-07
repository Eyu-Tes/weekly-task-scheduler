from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
  path('user/<int:pk>/task/<str:day>/', views.task_scheduler_view, name='user_home'),
  path('', views.sign_in, name='login'),
  path('register/', views.sign_up, name="register"),
  path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
  path('create_task/', views.CreateTaskView.as_view(), name='create_task'),
  path('update_task/', views.UpdateTaskView.as_view(), name='update_task'),
  path('delete_task/', views.DeleteTaskView.as_view(), name='delete_task'),
]
