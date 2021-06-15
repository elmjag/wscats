from django.urls import path
from pucks import views


urlpatterns = [
    path("", views.index, name="index"),
]
