"""
URL configuration for LMS project.

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
from django.urls import path, include, re_path
from personal import views as personal_views
from math_operations import views as m_operations

int_operations = [
    path('', m_operations.index),
    path('sum', m_operations.sum),
    path('sub', m_operations.sub),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw/', personal_views.index),
    path('test/', personal_views.test),
    path('test/<param1>/', personal_views.test),
    path('test/<param1>/<param2>/', personal_views.test),
    path('test/<param1>/<param2>/<param3>', personal_views.test),
    re_path(r'^(?P<int1>\d+)/(?P<int2>\d+)/', include(int_operations)),
]
