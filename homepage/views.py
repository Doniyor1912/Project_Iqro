from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from homepage.models import Service, ProcessStep, Ideas
from homepage.serializers import Serviceserializers, ProcessStepserializers, Ideasserializers




class HomepagePagination(PageNumberPagination):   # always used in List!
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000

@extend_schema_view(
    list=extend_schema(summary='list service', tags=['Service']),
    retrieve=extend_schema(summary='retrieve service', tags=['Service']),
    create=extend_schema(summary='create service', tags=['Service']),
    update=extend_schema(summary='update service', tags=['Service']),
    partial_update=extend_schema(summary='partial_update service', tags=['Service']),
    destroy=extend_schema(summary='destroy service', tags=['Service'])
)
class CRUDservice(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = Serviceserializers
    pagination_class = HomepagePagination
    filter_backends = [SearchFilter]
    search_fields = ['title']



@extend_schema_view(
    list=extend_schema(summary='list ideas', tags=['Ideas']),
    retrieve=extend_schema(summary='retrieve ideas', tags=['Ideas']),
    create=extend_schema(summary='create ideas', tags=['Ideas']),
    update=extend_schema(summary='update ideas', tags=['Ideas']),
    partial_update=extend_schema(summary='partial_update ideas', tags=['Ideas']),
    destroy=extend_schema(summary='destroy ideas', tags=['Ideas'])
)
class CRUDideas(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Ideas.objects.all()
    serializer_class = Ideasserializers
    pagination_class = HomepagePagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'role']


@extend_schema_view(
    list=extend_schema(summary='list processstep', tags=['ProcessStep']),
    retrieve=extend_schema(summary='retrieve processstep', tags=['ProcessStep']),
    create=extend_schema(summary='create processstep', tags=['ProcessStep']),
    update=extend_schema(summary='update processstep', tags=['ProcessStep']),
    partial_update=extend_schema(summary='partial_update processstep', tags=['ProcessStep']),
    destroy=extend_schema(summary='destroy processstep', tags=['ProcessStep'])
)
class CRUDprocessstep(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = ProcessStep.objects.all()
    serializer_class = ProcessStepserializers
    filter_backends = [SearchFilter]
    pagination_class = HomepagePagination
    search_fields = ['title']
