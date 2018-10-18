from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url('about/education/$', views.education, name='education'),
    url('about/work/$', views.work, name='work'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

