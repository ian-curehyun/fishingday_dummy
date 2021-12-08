from django.urls import path, include
from .views import helloAPI, randomPost

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomPost),
]