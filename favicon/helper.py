from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest

from favicon.models import Favicon


def get_favicon_of_site(site: Site):
    if type(site) != Site or not Site.objects.filter(pk=site.pk).exists():
        raise TypeError

    return Favicon.objects.filter(site=site, isFavicon=True).first()


def get_favicon_of_current_site(request: HttpRequest):
    return get_favicon_of_site(get_current_site(request))
