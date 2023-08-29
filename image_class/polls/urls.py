from django.urls import path

from . import views
# from .views import Data_entry

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='render'),
    path('ind/', views.ind, name='ind'),
    path('test/', views.test, name='test'),
    path('get_image/', views.get_image, name='get_image'),
    path ('data_save/', views.data_save, name="data_save"),
]
