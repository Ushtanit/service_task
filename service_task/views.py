# coding: utf-8
import json
import re
import urllib
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from service_task.models import SiteInfo


@csrf_exempt
def load_urls(request):
    if request.method == 'POST':
        try:
            urls = request.POST.items()[0][0].split(',')
        except Exception:
            return HttpResponse('wrong input')
        wrong_urls = ', wrong_urls: '
        for url in urls:
            try:
                response = urllib.urlopen(url).read()
                title = re.findall(r'<title>.+', response)[0].replace('<title>', '').replace('</title>', '')
                info = SiteInfo(title=title, url=url)
                info.save()
            except Exception:
                wrong_urls += url

        return HttpResponse('done{}'.format(wrong_urls))


def get_titles(request):
    info = list()
    for site in SiteInfo.objects.all():
        info.append(dict(url=site.url, title=site.title, timestamp=unicode(site.timestamp)))
    info = json.dumps(info, indent=4, separators=(',', ': '))
    return HttpResponse(info)
