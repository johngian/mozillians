import re

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from mozillians.common.middleware import safe_query_string
from mozillians.groups.models import Group


class OldGroupRedirectionMiddleware:
    """
    Redirect requests for groups from /group/<id>-<url> to
    /group/<url> to avoid breaking group urls with the new url
    schema.

    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        group_url = re.match('^/group/(?P<id>\d+)-(?P<url>[-\w]+)/$',
                             request.path_info)
        if (response.status_code == 404 and
                group_url and Group.objects.filter(url=group_url.group('url')).exists()):

            newurl = reverse('groups:show_group',
                             kwargs={'url': group_url.group('url')})
            if request.GET:
                with safe_query_string(request):
                    newurl += '?' + request.META['QUERY_STRING']
            return HttpResponseRedirect(newurl)
        return response
