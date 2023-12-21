from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_team", views.create_team, name="create_team"),
    path("edit_team/<int:team_id>", views.edit_team, name="edit_team"),
    path("delete_team/<int:team_id>", views.delete_team, name="delete_team"),
    path("create_member", views.create_member, name="create_member"),
    path("edit_member/<int:member_id>", views.edit_member, name="edit_member"),
    path("delete_member/<int:member_id>", views.delete_member, name="delete_member"),
]
