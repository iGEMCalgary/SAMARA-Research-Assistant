from django.urls import path

from . import views

urlpatterns = [
    path('', views.ModelList.as_view(), name='model_list'), # Sets model/ to display all modelling pages
    path('<int:pk>/', views.ModelDetailPage.as_view(), name='model_page'),  # Sets model/<identification key> to display detailed page
]