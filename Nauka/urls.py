from django.conf.urls import include, url
from django.contrib import admin
from contact.views import MessageAddView

urlpatterns = [
    # Examples:
    # url(r'^$', 'Nauka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^termometr/', include('Nauka.urls_termometr')),
    url(r'^odczyt/', include('Nauka.urls_odczyt')),
    url(r'^contact/$', MessageAddView.as_view())
]
