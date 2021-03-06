"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tweet import views
from tweet.views import tweet_list_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tweets/',include('tweet.urls')),
    url(r'^api/tweets/',include('tweet.api.urls',namespace='tweet-api')),
    url(r'^$',tweet_list_view.as_view(),name='home'),
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL,document_root=settings.STATIC_ROOT))
