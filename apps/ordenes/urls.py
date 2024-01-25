from django.urls import path
from . import views

urlpatterns = [
    path('nuevaorden/', views.nuevaorden_view, name='nuevaorden'),
    path('ordenregistrada/', views.ordenregistrada, name='ordenregistrada'),
]
