
from django.urls import path
from . import views


app_name = 'hive_manager'
urlpatterns = [
    path('', views.create_hive, name='create_hive'),
    path('', views.update_hive, name='update_hive'),
    path('', views.delete_hive, name='delete_hive'),
    path('', views.hive_detail, name='hive_detail'),

    path('<int:hive_id>', views.hive_detail, name='hive_detail'),
    path('<int:hive_id>', views.update_hive, name='update_hive'),
    path('<int:hive_id>', views.delete_hive, name='delete_hive'),


]
