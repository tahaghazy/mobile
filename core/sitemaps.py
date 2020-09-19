from django.contrib.sitemaps import Sitemap
from .models import Item
from django.shortcuts import reverse
from .views import ShopView
from .views import *
class PostSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8

    def items(self):
        return Item.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.post_update


class StaticViewSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8
    def items(self):
        return ['core:home']
    def location(self, item):
        return reverse(item)




