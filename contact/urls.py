from django.urls import path
from contact.views import *

urlpatterns = [

    # Service
    path('project/create-contact/', CRUDContact.as_view({'post': 'create'})),
    path('project/getlist-contact/', CRUDContact.as_view({'get': 'list'})),
    path('project/delete-contact/<int:pk>/', CRUDContact.as_view({'delete': 'destroy'})),
    path('project/get-contact/<int:pk>/', CRUDContact.as_view({'get': 'retrieve'})),
]