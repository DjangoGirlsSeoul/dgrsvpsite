from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader

from .models import Hack

def index(request):
	hacks = Hack.objects.order_by('-createdAt')

	context = {'hacks': hacks}
	return render(request,'hacks/hacks_home.html', context)

# To be changed later
def postSlug(request, slug):
	posts = Hack.objects.order_by('-createdAt')

	context = {'hacks': hacks}
	return render(request,'hacks/hacks_home.html', context)
