from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_team", views.create_team, name="create_team"),
    path("delete_team/<int:team_id", views.delete_team, name="delete_team"),
]
