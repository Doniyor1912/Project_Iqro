import os

from django.shortcuts import render

from rest_framework import mixins, status
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from .serializers import *
import telebot
from dotenv import load_dotenv

load_dotenv()

def send_telegram_message(message):
    chat_id = os.getenv('TELEGRAM_CHANNEL_ID', '')
    bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN', ''))
    bot.send_message(chat_id, message)

class ContactPagination(PageNumberPagination):   # always used in List!
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000


@extend_schema_view(
    list=extend_schema(summary='list contact project', tags=['Contact']),
    retrieve=extend_schema(summary='retrieve contact project', tags=['Contact']),
    create=extend_schema(summary='create contact project', tags=['Contact']),
    destroy=extend_schema(summary='destroy contact project', tags=['Contact']
))
class CRUDContact(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    pagination_class = ContactPagination

    def perform_create(self, serializer):
        instance = serializer.save()
        data = instance.created_at
        date = str(data)[0:10]
        time = str(data)[11:19]
        message = f"Contact ({date}/{time}): \nName: {instance.full_name}\nEmail: {instance.email_address}\nPhone: {instance.phone_number}\nsubject: {instance.subject}\nmessage: {instance.message}"
        return send_telegram_message(message)

