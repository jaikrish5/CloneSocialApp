from rest_framework import generics
from django.db.models import Q
from tweet.models import Tweet
from .serializers import TweetModelSerializer

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    queryset = Tweet.objects.all()

    def get_querset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                        Q(content__icontains = query) |
                        Q(user__username__icontains=query)
                        )
        return qs
