"""
URL configuration for Web_Project project.

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
from django.urls import path
from Home_App import views as hv

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", hv.home, name="home"),
    path('about/', hv.about, name='about'),
    path('contact/', hv.contact, name='contact'),
    path('menu/', hv.menu, name='menu'),
    path('about.html', hv.about, name='about_html'),
    path('menu.html', hv.menu, name='menu_html'),
    path('home.html', hv.home, name='home_html'),
    path('order.html', hv.order, name='order_html'),
    path('order/', hv.order, name='order'),

]