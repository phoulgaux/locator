from django.conf.urls import url, include
from rest_framework import routers
from locator.views import LocationViewSet


router = routers.DefaultRouter()
router.register(r'loc', LocationViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'rep9django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'locator.views.index'),
    url(r'^rest/', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^loc/$', 'locator.views.index'),
    url(r'^loc/([-@./#&+\w\s]*)$', 'locator.views.index')
]
