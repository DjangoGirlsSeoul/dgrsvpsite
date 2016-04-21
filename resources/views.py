import re
import requests
import bs4

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404,JsonResponse
from django.template import RequestContext, loader
from .models import Resource,Category
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned

URL_REGEX = r"""((?<=[^a-zA-Z0-9])(?:https?\:\/\/|[a-zA-Z0-9]{1,}\.{1}|\b)(?:\w{1,}\.{1}){1,5}(?:com|org|edu|gov|uk|net|ca|de|jp|fr|au|us|ru|ch|it|nl|se|no|es|mil|iq|io|ac|ly|sm){1}(?:\/[a-zA-Z0-9]{1,})*)"""
def index(request):
    resources = Resource.objects.order_by('-createdAt')
    context = {'resources': resources }
    return render(request,'resources/resources_home.html', context)

@csrf_exempt
def add_resource(request):
    if request.method == 'POST':
        response_json = {}
        token = request.POST['token']
        channel_name = request.POST['channel_name']
        user_name = request.POST['user_name']
        timestamp = request.POST['timestamp']
        text = request.POST['text']
        title = ''
        if token == settings.WEBHOOK_TOKEN:
            url_match = re.findall(URL_REGEX, text)
            if url_match:
                url = url_match[0]
                try:
                    r = requests.get(url, timeout=1)
                    html = bs4.BeautifulSoup(r.text, "html.parser")
                    title = html.title.text
                except:
                    e = sys.exc_info()[0]
                    print("Exception when getting url for slack resource, {}".format(e))
                finally:
                    response_json["text"] = saveResource(user_name, url, title)
                    response = JsonResponse(response_json)
                    return response
            else:
                print("no url")
        else :
            print("token does not match")

def saveResource(user_name, link, title):
    try:
        resource = Resource.objects.get(link=link)
        return "Saved already @{}".format(user_name)
    except ObjectDoesNotExist:
        resource = Resource(title=title,link=link)
        resource.save()
        return "Successfully saved @{}".format(user_name)
