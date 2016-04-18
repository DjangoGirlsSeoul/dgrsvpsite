from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader

from .models import Resource,Category

def index(request):
    resources = Resource.objects.order_by('-createdAt')
    context = {'resources': resources }
    return render(request,'resources/resources_home.html', context)
