
from django.urls import path
from . import views
from .views import HiveListView, HiveDetailView, HiveCreateView, HiveUpdateView, HiveDeleteView


# app_name = 'hive_manager'
urlpatterns = [
    # Hive URL
    path('new_hive/', HiveCreateView.as_view(), name='create_hive'),
    path('hive_list/', HiveListView.as_view(), name='hive_list'),
    path('hive_detail/<int:pk>', HiveDetailView.as_view(), name='hive_detail'),
    path('hive_update/<int:pk>', HiveUpdateView.as_view(), name='hive_update'),
    path('hive_delete/<int:pk>', HiveDeleteView.as_view(), name='hive_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('create_hive/', views.create_hive, name='create_hive'),
    # path('update_hive/<int:hive_id>', views.update_hive, name='update_hive'),
    # path('delete_hive/<int:hive_id>', views.delete_hive, name='delete_hive'),
    # path('hive_detail/<int:hive_id>', views.hive_detail, name='hive_detail'),
    # path('hive_list/', views.hive_list, name='hive_list'),



    # Task URL
    path('create_task/', views.create_task, name='create_task'),
    path('update_task/<int:task_id>', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('task_detail/<int:task_id>', views.task_detail, name='task_detail'),
    path('task_list/', views.task_list, name='task_list'),

    # path('<int:hive_id>', views.hive_detail, name='hive_detail'),
    # path('<int:hive_id>', views.update_hive, name='update_hive'),
    # path('<int:hive_id>', views.delete_hive, name='delete_hive'),


]
