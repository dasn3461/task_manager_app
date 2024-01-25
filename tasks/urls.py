from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Create the REST API URLs   
    path('tasks/', views.TaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskRetrieveAPIView.as_view(), name='task-detail'),
    path('tasks/create/', views.TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDestroyAPIView.as_view(), name='task-delete'),
]

    



