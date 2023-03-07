from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, price, about, testify

urlpatterns=[
    path('', index, name='home'),
    path('testimonies/', testify, name='testimonies'),
    path('about/', about, name='about'),
    path('pricing/', price, name='price'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)