from django.urls import re_path, path
from pucks import consumers


websocket_urlpatterns = [
    path("ws/pucks", consumers.CatsPucks.as_asgi()),
]
