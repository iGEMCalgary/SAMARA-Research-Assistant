from django.urls import path

from . import views

urlpatterns = [
    path('', views.softwarelist.as_view(), name='software_list'),
    path('software/', views.softpage, name='software_page'),

]