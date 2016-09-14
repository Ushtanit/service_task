# coding: utf-8
import requests
import json
import lxml.html as html
import lxml.etree as etree
import re
import urllib
from django.http import HttpResponse
from service_task.models import SiteInfo
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def load_urls(request):
    if request.method == 'POST':
        urls = ['https://docs.djangoproject.com/en/1.10/intro/tutorial02/', 'https://vk.com/themusicend']
        for url in urls:
            response = urllib.urlopen(url).read()
            title = re.findall(r'<title>.+', response)[0].replace('<title>', '').replace('</title>', '')
            info = SiteInfo(title=title, url=url)
            info.save()
    return HttpResponse('done')


def get_titles(request):
    info = list()
    for site in SiteInfo.objects.all():
        info.append(dict(url=site.url, title=site.title, timestamp=unicode(site.timestamp)))
    info = json.dumps(info, indent=4, separators=(',', ': '))
    return HttpResponse(info)
