from django.conf.urls import url
from Home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.Home, name='Home'),
    url(r'^login/$', views.Login, name='Login'),
    url(r'^agenda/proximos/$', views.Proximos, name='Proximos'),
    url(r'^agenda/proximos/informacion/$', views.Informacionproxima, name='Informacionproxima'),
    url(r'^agenda/pasados/$', views.Pasados, name='Pasados'),
    url(r'^agenda/pasados/informacion/$', views.Informacionpasada, name='Informacionpasada'),
    url(r'^publicar/$', views.Publicar, name='Publicar'),
    url(r'^quienessomos/$', views.Quienes, name='Quienes'),
    url(r'^conocenos/$', views.Conocenos, name='Conocenos'),
    url(r'^contacto/$', views.Contacto, name='Contacto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)