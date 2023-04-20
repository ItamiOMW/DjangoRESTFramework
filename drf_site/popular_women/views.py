from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Woman, Category
from .serializers import WomanSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class WomanAPIListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 100


class WomanAPIList(generics.ListCreateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomanAPIListPagination


class WomanAPIUpdate(generics.UpdateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = (IsAuthenticated,)


class WomanApiDestroy(generics.DestroyAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = (IsAdminOrReadOnly,)

# class WomanViewSet(viewsets.ModelViewSet):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Woman.objects.all()[:3]
#
#         return Woman.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         return Response({'categories': category.name})
