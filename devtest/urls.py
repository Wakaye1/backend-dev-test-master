"""devtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app.crm.tasks import create_client # comment out
from app.crm.views import all_clients


urlpatterns = [
    path('', all_clients, name="all_clients"),
    path('admin/', admin.site.urls),
    path('crm/', include('app.crm.urls')),
]

# 3600s is a day
create_client(repeat = 3600, repeat_until = None) # comment out
