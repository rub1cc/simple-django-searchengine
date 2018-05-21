from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class GoogleSearchAppHook(CMSApp):
    name = _("Google Custom Search")
    urls = ["googlesearch.urls"]

apphook_pool.register(GoogleSearchAppHook)
