from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse, Http404
from django.template import RequestContext

from django.contrib.auth.models import User

import datetime

from django.shortcuts import render_to_response
from mysite.forms import ContactForm

def display_meta(request):
	values = {'meta': request.META.items()}
	template = get_template('meta.html')
	return HttpResponse(template.render(values))

def hello(request):
	return HttpResponse("Hello World")

def current_datetime(request):
	now = datetime.datetime.now()
	template = get_template('current_datetime.html')
	html = {'current_date': now}
	return HttpResponse(template.render(html))

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	# assert False
	template = get_template('current_datetime.html')
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = {'offset': offset, 'dt': dt}
	return HttpResponse(template.render(html))

def dev(request):
	dev = 'ROY'
	template = get_template('current_datetime.html')
	html = {'dev': dev}
	return HttpResponse(template.render(html))

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('e-mail', 'noreply@example.com'),
				['siteowner@example.com'],)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(initial={'subject': 'I like the site!'})
	return render_to_response('contact_form.html', {'form': form})


def users_list(request):
	users = User.objects.all()
	# users = User.objects.values()
	# staff_users = User.objects.filter(groups_name='Staff')
	# admin_users = User.objects.filter(groups_name='Admin')
	return render_to_response('users_list.html', {'users': users})


def custom_proc(request):
	"A context processor that provides 'app', 'user' and 'ip_address'."
	return {
	'app': 'My app',
	'user': request.user,
	'ip_address': request.META['REMOTE_ADDR']
	}

def view_1(request):
# ...
	t = get_template('template1.html')
	c = RequestContext(request, {'message': 'I am view 1.'},processors=[custom_proc])
	html = {'c':c}
	return HttpResponse(t.render(html))

def view_2(request):
# ...
	t = get_template('template2.html')
	c = RequestContext(request, {'message': 'I am the second view.'},processors=[custom_proc])
	html = {'c': c}
	return HttpResponse(t.render(html))
