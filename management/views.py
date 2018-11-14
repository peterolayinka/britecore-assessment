from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

from .models import Risk, RiskField
from .serializers import RiskSerializer

from rest_framework import viewsets
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html', {})
class RiskViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    def get_queryset(self, *args, **kwargs):
        return Risk.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = RiskSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        serializer = RiskSerializer(self.get_queryset().filter(pk=pk), many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass