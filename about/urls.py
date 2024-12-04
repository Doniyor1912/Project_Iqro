from django.urls import path
from about.views import *

urlpatterns = [

    # CompanyInfo
    path('project/create-company/', CRUDCompany.as_view({'post': 'create'})),
    path('project/getlist-company/', CRUDCompany.as_view({'get': 'list'})),
    path('project/put-company/<int:pk>/', CRUDCompany.as_view({'put': 'update'})),
    path('project/patch-company/<int:pk>/', CRUDCompany.as_view({'patch': 'partial_update'})),
    path('project/delete-company/<int:pk>/', CRUDCompany.as_view({'delete': 'destroy'})),
    path('project/get-company/<int:pk>/', CRUDCompany.as_view({'get': 'retrieve'})),

    # TeamMember
    path('project/create-company/', CRUDTeammember.as_view({'post': 'create'})),
    path('project/getlist-company/', CRUDTeammember.as_view({'get': 'list'})),
    path('project/put-company/<int:pk>/', CRUDTeammember.as_view({'put': 'update'})),
    path('project/patch-company/<int:pk>/', CRUDTeammember.as_view({'patch': 'partial_update'})),
    path('project/delete-company/<int:pk>/', CRUDTeammember.as_view({'delete': 'destroy'})),
    path('project/get-company/<int:pk>/', CRUDTeammember.as_view({'get': 'retrieve'})),

]
