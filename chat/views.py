from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message

@api_view(["POST"])
def receive_message(request):
    usuario = request.data.get("usuario")
    puntos = request.data.get("puntos")

    message = Message.objects.create(usuario=usuario, puntos=puntos)
    return Response({"message": "Saved successfully!"})

@api_view(["GET"])
def get_messages(request):
    messages = Message.objects.order_by("-timestamp")[:50]  # Get last 50 messages
    return Response({"messages": [{"usuario": msg.usuario, "puntos": msg.puntos, "timestamp": msg.timestamp} for msg in messages]})