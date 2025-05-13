
from django.urls import path
from hdgroup import views


urlpatterns = [
    path('', views.index, name='index'),
]