from django.urls import path
from .views import inbox_view, send_message_view

urlpatterns = [
    path('inbox/', inbox_view, name='inbox'),
    path('send/', send_message_view, name='send-message'),
]