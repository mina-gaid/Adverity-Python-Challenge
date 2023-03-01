from django.urls import path

from . import views

app_name = 'starwars'

urlpatterns = [
    path('', views.collections_list, name='collections_list'),
    path('datasets/<int:dataset_id>/', views.collections_detail, name='collections_detail'),
    path('download-data/', views.download_data, name='download_data'),
]