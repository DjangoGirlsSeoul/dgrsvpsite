from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader


def index(request):
    context = ''
    return render(request,'landingsite/index.html', context)
