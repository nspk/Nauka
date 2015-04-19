from django.conf.urls import include, url

from temp.views import OdczytListView

urlpatterns = [
    url(r'^$', OdczytListView.as_view(), name='odczyt-list')
]