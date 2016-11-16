# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import render_to_response, render
from django.template import Context, RequestContext
import os

def index(request):

	static_html = 'test.html'
	context = {}
	if not os.path.exists(static_html):
		content = render_to_string('index.html', context)
		with open(static_html, 'w') as static_file:
			static_file.write(content)

	return render(request, static_html)