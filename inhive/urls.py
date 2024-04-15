"""
URL configuration for in_hive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from hive_manager import views
# from hive_manager.views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('hive_manager.urls')),
    # path('hive_list/', include('hive_manager.urls')),
    # path('hive_detail/', include('hive_manager.urls')),
    # path('update_hive/', include('hive_manager.urls')),
    # path('delete_hive/', include('hive_manager.urls')),


]
urlpatterns += staticfiles_urlpatterns()
