from django.urls import path
from . import views

urlpatterns = [
    path('', views.PainelTemplate.as_view())
]
