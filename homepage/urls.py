from django.urls import path

from homepage.views import CRUDservice, CRUDideas, CRUDprocessstep

url_patterns = [

    # Service
    path('project/create-service/', CRUDservice.as_view({'post': 'create'})),
    path('project/getlist-service/', CRUDservice.as_view({'get': 'list'})),
    path('project/put-service/<int:pk>/', CRUDservice.as_view({'put': 'update'})),
    path('project/patch-service/<int:pk>/', CRUDservice.as_view({'patch': 'partial_update'})),
    path('project/delete-service/<int:pk>/', CRUDservice.as_view({'delete': 'destroy'})),
    path('project/get-service/<int:pk>/', CRUDservice.as_view({'get': 'retrieve'})),


    # Ideas
    path('project/create-ideas/', CRUDideas.as_view({'post': 'create'})),
    path('project/getlist-ideas/', CRUDideas.as_view({'get': 'list'})),
    path('project/put-ideas/<int:pk>/', CRUDideas.as_view({'put': 'update'})),
    path('project/patch-ideas/<int:pk>/', CRUDideas.as_view({'patch': 'partial_update'})),
    path('project/delete-ideas/<int:pk>/', CRUDideas.as_view({'delete': 'destroy'})),
    path('project/get-ideas/<int:pk>/', CRUDideas.as_view({'get': 'retrieve'})),

    # Processstep
    path('project/create-processtep/', CRUDprocessstep.as_view({'post': 'create'})),
    path('project/getlist-processtep/', CRUDprocessstep.as_view({'get': 'list'})),
    path('project/put-processtep/<int:pk>/', CRUDprocessstep.as_view({'put': 'update'})),
    path('project/patch-processtep/<int:pk>/', CRUDprocessstep.as_view({'patch': 'partial_update'})),
    path('project/delete-processtep/<int:pk>/', CRUDprocessstep.as_view({'delete': 'destroy'})),
    path('project/get-processtep/<int:pk>/', CRUDprocessstep.as_view({'get': 'retrieve'})),

]