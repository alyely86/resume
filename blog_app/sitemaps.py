from django.contrib import sitemaps
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from .models import Post

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["post_blog", "contact", "resume"]

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED)

    def lastmod(self, obj):
        return obj.publish