from django.conf.urls import include, url
from django.contrib import admin

from temp.views import TermometrListView

urlpatterns = [
    # Examples:
    # url(r'^$', 'Nauka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^termometr/', TermometrListView.as_view())
]
