
from django.urls import path
from . import views

urlpatterns = [
    path('create_hive/', views.create_hive, name='create_hive'),
    path('hive_detail/<int:hive_id>/', views.hive_detail, name='hive_detail'),
    path('update/<int:hive_id>/', views.update_hive, name='update_hive'),
    path('delete/<int:hive_id>/', views.delete_hive, name='delete_hive'),


]
