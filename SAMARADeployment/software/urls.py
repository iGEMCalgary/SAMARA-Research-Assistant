from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('software/', views.softpage, name='software_page'),
]