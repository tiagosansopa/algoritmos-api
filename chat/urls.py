from django.urls import path
from .views import receive_message, get_messages

urlpatterns = [
    path("message/", receive_message),
    path("messages/", get_messages),
]