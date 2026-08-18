from django.urls import path
from . import views

urlpatterns = [
   path("", views.article_list, name="article_list"),
   path("articles/<slug:slug>/",  views.article_detail, name="article_detail"),
   path("article/create/", views.article_create, name="article_create"),
   path("articles/<slug:slug>/edit/", views.article_edit, name="article_edit"),
   path("articles/<slug:slug>/delete/", views.article_delete, name="article_delete"),
]
