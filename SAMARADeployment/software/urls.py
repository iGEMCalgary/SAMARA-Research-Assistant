from django.urls import path

from . import views

urlpatterns = [
    path('', views.SoftwareList.as_view(), name='software_list'),
    path('<int:pk>', views.DetailSoftPage.as_view(), name='software_page'),

]