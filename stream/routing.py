from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('', consumers.Streamer.as_asgi()),
]