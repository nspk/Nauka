from django.conf.urls import include, url

from temp.views import TermometrListView, TermometrDetailView

urlpatterns = [
    url(r'^$', TermometrListView.as_view(), name='termometr-list'),
    url(r'^(?P<pk>\d+)/$', TermometrDetailView.as_view(), name='termometr-detail')
]
