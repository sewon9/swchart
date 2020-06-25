from django.contrib import admin
from django.urls import path, include
from chart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         views.home, name='home'),
    path('covid/', views.covid, name='covid'),
    path('covid2/', views.covid2, name='covid2'),
    path('covid3/', views.covid3, name='covid3'),
]

