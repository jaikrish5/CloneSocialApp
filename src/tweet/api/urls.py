# from django.conf.urls import url,include
# from django.views.generic.base import RedirectView
# from .views import tweet_detail_view,tweet_list_view,tweet_create_view,tweet_update_view,tweet_delete_view
from django.conf.urls import url,include
from .views import TweetListAPIView

urlpatterns=[
url(r'^$',TweetListAPIView.as_view(),name='list'),
# # url(r'^$',RedirectView.as_view(url="/")),
# url(r'^(?P<pk>\d+)/$',tweet_detail_view.as_view(),name='detail'),
# url(r'^$',tweet_list_view.as_view(),name='list'),
# url(r'^create/$',tweet_create_view.as_view(),name='create'),
# url(r'^update/(?P<pk>\d+)$',tweet_update_view.as_view(),name='update'),
# url(r'^delete/(?P<pk>\d+)$',tweet_delete_view.as_view(),name='delete'),


]
