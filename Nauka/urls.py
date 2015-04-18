from django.conf.urls import include, url
from django.contrib import admin

from temp.views import TermometrListView, OdczytListView, TermometrDetailView

urlpatterns = [
    # Examples:
    # url(r'^$', 'Nauka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^termometr/', TermometrListView.as_view(), name='termometr-list'),
    url(r'^odczyt/', OdczytListView.as_view(), name='odczyt-list'),
    url(r'^termometr/(?P<pk>\d+)/$', TermometrDetailView.as_view(), name='termometr-detail')
]
