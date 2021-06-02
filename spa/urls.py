from django.urls import path

from spa import views

urlpatterns = [
    path('', views.index, name='index'),
]