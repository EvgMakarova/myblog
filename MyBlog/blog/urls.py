from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('xd/', views.PostView.indexX),
    path('add/', views.PostView.add, name='add')
]