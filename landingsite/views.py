from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.mail import send_mail, BadHeaderError

def index(request):
        context = ''
        return render(request,'landingsite/index.html', context)

def contact(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')
        subject = 'Get in touch - Code For Everyone website'
        if subject and message and from_email and full_name:
            try:
                message += "\n From: " + full_name + "\n Email: " + from_email
                send_mail(subject, message, from_email, ['info@codeforeveryone.co'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('contact-us/thanks/')
        else:
            return HttpResponseRedirect('contact-us/')
    else:
        return HttpResponseRedirect('/')
