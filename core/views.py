from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Locode
from .serializers import LocodeSerializer
from .filters import LocodeFilter


class LocodeView(ModelViewSet):

    serializer_class = LocodeSerializer
    filterset_class = LocodeFilter
    queryset = Locode.objects.all()
