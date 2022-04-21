from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.ice_cream_list),
    path('group/<slug:slug>/', views.ice_cream_detail),
]
