from django.urls import path
from project.views import *


urlpatterns = [
    #Project
    path('project/getlist-project/', CRUDProject.as_view({'get': 'list'})),
    path('project/get-project/<int:pk>/', CRUDProject.as_view({'get': 'retrieve'})),

    #Category
    path('project/create-category/', CRUDCategory.as_view({'post': 'create'})),
    path('project/getlist-category/', CRUDCategory.as_view({'get': 'list'})),
    path('project/put-category/<int:pk>/', CRUDCategory.as_view({'put': 'update'})),
    path('project/patch-category/<int:pk>/', CRUDCategory.as_view({'patch': 'partial_update'})),
    path('project/delete-category/<int:pk>/', CRUDCategory.as_view({'delete': 'destroy'})),
    path('project/get-category/<int:pk>/', CRUDCategory.as_view({'get': 'retrieve'})),

    # Project Details
    path('project/create-projectdetails/', CRUDProjectDetails.as_view({'post': 'create'})),
    path('project/getlist-projectdetails/', CRUDProjectDetails.as_view({'get': 'list'})),
    path('project/put-projectdetails/<int:pk>/', CRUDProjectDetails.as_view({'put': 'update'})),
    path('project/patch-projectdetails/<int:pk>/', CRUDProjectDetails.as_view({'patch': 'partial_update'})),
    path('project/delete-projectdetails/<int:pk>/', CRUDProjectDetails.as_view({'delete': 'destroy'})),
    path('project/get-projectdetails/<int:pk>/', CRUDProjectDetails.as_view({'get': 'retrieve'})),

    # Project Showcase
    path('project/getlist-projectshowcase/', CRUDProjectShowcase.as_view({'get': 'list'})),
    path('project/get-projectshowcase/<int:pk>/', CRUDProjectShowcase.as_view({'get': 'retrieve'})),
]