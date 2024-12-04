from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from .serializers import *


class ProjectPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000

@extend_schema_view(
    list=extend_schema(summary='List project', tags=['Project']),
    retrieve=extend_schema(summary='Retrieve project', tags=['Project']))
class CRUDProject(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = ProjectSerializers
    pagination_class = ProjectPagination
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    search_fields = ['title']



    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Project.objects.all()

        return Project.objects.filter(pk=pk)


@extend_schema_view(
    list=extend_schema(summary='List Category', tags=['Category']),
    retrieve=extend_schema(summary='Retrieve Category', tags=['Category']),
    create=extend_schema(summary='Create Category', tags=['Category']),
    update=extend_schema(summary='Update Category', tags=['Category']),
    partial_update=extend_schema(summary='Partial_update Category', tags=['Category']),
    destroy=extend_schema(summary='Destroy Category', tags=['Category'])
)
class CRUDCategory(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = CategorySerializers
    filter_backends = [SearchFilter]
    pagination_class = ProjectPagination
    search_fields = ['name']



    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Category.objects.all()

        return Category.objects.filter(pk=pk)


@extend_schema_view(
    list=extend_schema(summary='List project Details', tags=['Project details']),
    retrieve=extend_schema(summary='Retrieve project Details', tags=['Project details']),
    create=extend_schema(summary='Create project Details', tags=['Project details']),
    update=extend_schema(summary='Update project Details', tags=['Project details']),
    partial_update=extend_schema(summary='Partial_update project Details', tags=['Project details']),
    destroy=extend_schema(summary='Destroy project Details', tags=['Project details']
))
class CRUDProjectDetails(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = ProjectDetailsSerializers
    filter_backends = [SearchFilter]
    pagination_class = ProjectPagination
    search_fields = ['title']


    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Project.objects.all()

        return Project.objects.filter(pk=pk)

@extend_schema_view(
    list=extend_schema(summary='List project Showcase', tags=['Project Showcase']),
    retrieve=extend_schema(summary='Retrieve project Showcase', tags=['Project Showcase'])
)
class CRUDProjectShowcase(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = ProjectSerializers
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class = ProjectPagination



    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Project.objects.all()

        return Project.objects.filter(pk=pk)

@extend_schema_view(
    create=extend_schema(summary='Update', tags=['Update-image'])
)

class CUpdateimage(mixins.CreateModelMixin,
                   GenericViewSet):
    serializer_class = UpdateimageSerializers
    queryset = Updateimage.objects.all()
