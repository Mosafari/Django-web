from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.resolpi, name='resolpi'),
    path('', views.resopy, name='resopy'),
    path('', views.resoflask, name='resoflask'),
    path('', views.resodjango, name='resodjango')
]