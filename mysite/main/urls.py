from django.urls import path
from . import views

urlpatterns = [
    path("", views.html_template),
    #path("", views.index, name="index"),
    path("v1/", views.view1, name="view1"),
]
