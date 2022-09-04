from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("blogs", views.blog_index, name="blog_index"),
    path("blogs/<int:pk>/", views.blog_detail, name="blog_detail"),
]
