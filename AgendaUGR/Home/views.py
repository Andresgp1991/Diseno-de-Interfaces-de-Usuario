from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.core.files import File
from os.path import basename
from tempfile import TemporaryFile
from urllib.parse import urlsplit
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from mimetypes import guess_type
from django.http import HttpResponse
from AgendaUGR.settings import MEDIA_ROOT
from django.template import Context, loader

# Create your views here.

# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]

mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]


def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''

    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]

    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True

    return mobile_browser

def Home(request):

    if mobileBrowser(request):
        t = loader.get_template('mhome.html')
    else:
        t = loader.get_template('home.html')

    return HttpResponse(t.render())

def Login(request):
    return render(request, 'login.html')

def Proximos(request):
    return render(request, 'proximos.html')

def Pasados(request):
    return render(request, 'pasados.html')

def Publicar(request):
    return render(request, 'publicar.html')

def Quienes(request):
    return render(request, 'quienes.html')

def Conocenos(request):
    return render(request, 'conocenos.html')

def Contacto(request):
    return render(request, 'contacto.html')

def Informacionproxima(request):
    return render(request, 'informacionproxima.html')

def Informacionpasada(request):
    return render(request, 'informacionpasada.html')