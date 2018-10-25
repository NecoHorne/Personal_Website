from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from Neco.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^contact/$', views.contact, name='contact'),
                  url(r'^about/$', views.about, name='about'),
                  url(r'^portfolio/$', views.portfolio, name='portfolio'),
                  url(r'^thanks/$', views.thanks, name='thanks'),
                  url('about/education/$', views.education, name='education'),
                  url('about/work/$', views.work, name='work'),
                  url(r'^googleeb483e5f93dd14b7.html$', views.google, name='google'),
                  url(r'^sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
                  url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
                      name="robots_file"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
