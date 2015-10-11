"""Load static content for Flatpages rather than Hardcode URL"""
from django import template
from django.template import Template, Context
from django.template import RequestContext
from django.template.defaultfilters import stringfilter
from django.conf import settings
register = template.Library()

@register.filter
@stringfilter
def load_static(val):
	#There's a better way to do this. Must investigate.
	#anyways we create template object, and pass it data via context and fill it with render
	tval = Template(val)
	con = Context({'STATIC_URL': settings.STATIC_URL})
	return tval.render(con)


@register.filter
@stringfilter
def load_static_ref(val):
	context = RequestContext(val, {'STATIC_URL':settings.STATIC_URL})
	return context
