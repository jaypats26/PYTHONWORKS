from django.urls import path

from . import views

app_name="artblog"
urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts"),
    path("detailposts", views.detailposts, name="detailposts")
]