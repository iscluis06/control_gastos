"""control_gastos URL Configuration

The `urlpatterns` list routes URLs to views_classes. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views_classes
    1. Add an import:  from my_app import views_classes
    2. Add a URL to urlpatterns:  path('', views_classes.home, name='home')
Class-based views_classes
    1. Add an import:  from other_app.views_classes import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('control_gastos/', include("control_gastos.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
