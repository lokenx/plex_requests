from django.conf.urls import url, include
from django.contrib import admin
from movies import views as movie_views
from config import views as config_views


urlpatterns = [
    url(r'^api/auth/', include('rest_framework.urls')),
    url(r'^api/movies/$', movie_views.MovieList.as_view()),
    url(r'^api/movies/(?P<pk>[0-9]+)/$', movie_views.MovieDetail.as_view()),
    url(r'^api/settings/(?P<singleton_enforce>[0-9]+)/$', config_views.ConfigList.as_view()),
    url(r'^admin/', admin.site.urls),
]
