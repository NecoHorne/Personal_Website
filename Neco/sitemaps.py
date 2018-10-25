from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):

    def items(self):
        return ['index', 'contact', 'about', 'portfolio', 'education', 'work']

    def priority(self, item):
        if item == 'index':
            return 1.0
        else:
            return 0.6

    def location(self, item):
        return reverse(item)
