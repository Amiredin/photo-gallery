from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^searching/', views.search_results, name='searching'),
    url(r'^filter/', views.location_filter, name='location_filter'),
    url(r'^perimage/(\d+)', views.singleimage, name='image'),
    ]
    
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)