from django.urls import path
from . import views

urlpatterns = [
    #dejar en la raíz
    path('', views.services, name="services"),
]
