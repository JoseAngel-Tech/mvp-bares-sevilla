from rest_framework import viewsets

from .models import Bar
from .serializers import BarSerializer


class BarViewSet(viewsets.ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer