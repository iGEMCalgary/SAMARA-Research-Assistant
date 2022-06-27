from django.urls import path

from . import views

app_name = 'software'
urlpatterns = [
    path('', views.SoftwareList.as_view(), name='software_list'),
    path('<int:pk>', views.SoftwareDetailPage.as_view(), name='software_page'),

]