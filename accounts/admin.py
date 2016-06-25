from django.contrib import admin, messages
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string, get_template

FROM_EMAIL = "seoul+registration@djangogirls.org"
EMAIL_SUBJECT = "{}, You're In!"

class CustomUserAdmin(UserAdmin):
    actions = ['approve_and_email']

    def approve_and_email(self, request, queryset):
        queryset.update(is_active=True)
        user = []
        for user in queryset:
            email_context = {'username': user.username, 'user_id': user.id }
            message = get_template('registration/approved_email.html').render(Context(email_context))
            email = EmailMultiAlternatives(EMAIL_SUBJECT.format(user.username), '' , FROM_EMAIL, [user.email])
            email.attach_alternative(message, "text/html")
            try:
                email.send()
            except Exception as e:
                self.message_user(request, "Sending Email failed for {} - {}".format(user.username, e))

    approve_and_email.short_description = "Approve and Email User(s)"

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
