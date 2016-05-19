from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserCreateForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string, get_template

FROM_EMAIL = "seoul+registration@djangogirls.org"
EMAIL_SUBJECT = "New User Registered - {}"

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            # login(request, user)
            messages.add_message(request, messages.INFO, 'Thank you for registering! Please wait until we approve your registration.', 'message register-success')
            
            email_context = {'username': username, 'user_id': user.id }
            message = get_template('registration/register_email.html').render(Context(email_context))
            email = EmailMultiAlternatives(EMAIL_SUBJECT.format(username), '' , FROM_EMAIL, [FROM_EMAIL])
            email.attach_alternative(message, "text/html")
            try:
                email.send()
            except Exception as e:
                print("email failed - {}".format(e))
            return HttpResponseRedirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', { 'form': form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
