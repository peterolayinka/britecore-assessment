from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

from .models import Risk, RiskFieldType, RiskType, RiskField
from .serializers import RiskSerializer, RiskFieldTypeSerializer, RiskTypeSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

def index(request):
    risks = Risk.objects.all()
    page = request.POST.get('page')
    paginator = Paginator(risks, 10)
    try:
        risks = paginator.page(page)
    except PageNotAnInteger:
        risks = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return None
        risks = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'risks': risks})
    
# @method_decorator(csrf_exempt, name='dispatch') 
class RiskViewSet(viewsets.ViewSet):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(RiskViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return Risk.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = RiskSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    # @csrf_exempt
    def create(self, request):
        post_data = request.data
        try:
            risk=Risk.objects.create(client_name=post_data['clientName'], risk_type_id=post_data['riskType'])
            risk_field = RiskField.objects.bulk_create([RiskField(field_type_id=x.get('field'), risk=risk, value=x.get('value')) for x in post_data['fields']])
            status = True
        except:
            status = False
        return Response({"status": status})

    def retrieve(self, request, pk=None):
        try:
            serializer = RiskSerializer(self.get_queryset().filter(pk=pk), many=True)
            return Response(serializer.data)
        except:
            raise Http404

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class RiskTypeViewSet(viewsets.ViewSet):
    def get_queryset(self, *args, **kwargs):
        return RiskType.objects.all()

    def list(self, request, *args, **kwargs):
        risk_types = RiskTypeSerializer(self.get_queryset(), many=True)
        field_types = RiskFieldTypeSerializer(RiskFieldType.objects.all(), many=True)
        return Response({'risk_types':risk_types.data,'field_types': field_types.data})