
from django.urls import path
from api_examples import views

urlpatterns = [
    path('', views.index, name='index'),
]

