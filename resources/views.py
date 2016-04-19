from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404,JsonResponse
from django.template import RequestContext, loader
from .models import Resource,Category
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned

def index(request):
    resources = Resource.objects.order_by('-createdAt')
    context = {'resources': resources }
    return render(request,'resources/resources_home.html', context)

@csrf_exempt
def add_resource(request):
    if request.method == 'POST':
        responseJson = {}
        token = request.POST['token']
        channel_name = request.POST['channel_name']
        trigger_word = request.POST['trigger_word']
        if token == settings.WEBHOOK_TOKEN and channel_name == "learning-resources" and trigger_word == "resource":
            user_name = request.POST['user_name']
            timestamp = request.POST['timestamp']
            text = request.POST['text']
            print(user_name,text,trigger_word)
            result = saveResource(text)
            responseJson["text"] = result.format(user_name)
            response = JsonResponse(responseJson)
            return response
        else :
            print("token does not match")

def saveResource(text):
    textArray = text.split()
    #ref: ['resource', '-title:', 'visualgo', 'category:', 'algorithm', 'link:', 'http://visualgo.net/']
    if len(textArray) >= 7 and "http" in textArray[6]:
        link = textArray[6]
        print(link)
        category = textArray[4].lower()
        try:
            cat = Category.objects.get(title=category)
            print("cat :",cat)
        except ObjectDoesNotExist:
            cat = Category(title=category)
            cat.save()
        try:
            resource = Resource.objects.get(link=link)
            return "Resource saved already @{}"
        except ObjectDoesNotExist:
            resource = Resource(title=textArray[2],link=link,category=cat)
            resource.save()
            return "Resource successfully saved @{}"

    else :
        return "This resource is not properly formatted @{}"
