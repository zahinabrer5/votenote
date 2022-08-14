from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("poll/<str:id>", views.poll, name="poll"),
    path("create", views.create, name="create"),
    path("list", views.list, name="list"),
]
