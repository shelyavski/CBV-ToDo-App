from django.urls import path, include
from .views import TasksListView, TaskCreateView, TaskEditView, TaskDeleteView
from .user_views import UserLoginView, UserRegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks-view'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('edit/<int:pk>/', TaskEditView.as_view(), name='task-edit'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),

    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(next_page='user-login'), name='user-logout'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
]
