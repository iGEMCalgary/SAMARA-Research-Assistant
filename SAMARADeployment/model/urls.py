from django.urls import path

from . import views

urlpatterns = [
    path('', views.ModelList.as_view(), name='model_list'),
    path('<int:pk>/', views.ModelDetailPage.as_view(), name='model_page'),

]