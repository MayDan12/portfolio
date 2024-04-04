
from django.urls import path
from . import views
from .views import (HiveListView,
                    HiveDetailView,
                    HiveCreateView,
                    HiveUpdateView,
                    HiveDeleteView,
                    TaskListView,
                    TaskDetailView,
                    TaskCreateView, TaskUpdateView, TaskDeleteView, UserHiveListView)


# app_name = 'hive_manager'
urlpatterns = [
    # Hive URL
    path('new_hive/', HiveCreateView.as_view(), name='create_hive'),
    path('hive_list/', HiveListView.as_view(), name='hive_list'),
    path('hive_detail/<int:pk>', HiveDetailView.as_view(), name='hive_detail'),
    path('hive_update/<int:pk>', HiveUpdateView.as_view(), name='hive_update'),
    path('hive_delete/<int:pk>', HiveDeleteView.as_view(), name='hive_delete'),
    path('user_hive_list/<str:username>', UserHiveListView.as_view(), name='user_hive_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('create_hive/', views.create_hive, name='create_hive'),
    # path('update_hive/<int:hive_id>', views.update_hive, name='update_hive'),
    # path('delete_hive/<int:hive_id>', views.delete_hive, name='delete_hive'),
    # path('hive_detail/<int:hive_id>', views.hive_detail, name='hive_detail'),
    # path('hive_list/', views.hive_list, name='hive_list'),



    # Task URL
    path('task_list/', TaskListView.as_view(), name='task_list'),
    path('task_update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('task_delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('task_detail/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('new_task/', TaskCreateView.as_view(), name='create_task'),

    # path('<int:hive_id>', views.hive_detail, name='hive_detail'),
    # path('<int:hive_id>', views.update_hive, name='update_hive'),
    # path('<int:hive_id>', views.delete_hive, name='delete_hive'),


]
