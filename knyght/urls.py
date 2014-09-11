from django.conf.urls import include, url
from django.contrib import admin

from pages.views import DetailView, home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<url>[\w/-]+)$', DetailView.as_view(), name='page'),
]
