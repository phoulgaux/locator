from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'rep9django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'([-@./#&+\w\s]*)', 'locator.views.index')
]
