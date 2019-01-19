from rest_framework import serializers

from tweet.models import Tweet
from accounts.api.serializers import UserDisplaySerializer

class TweetModelSerializer(serializers.ModelSerializer):
    user =  UserDisplaySerializer()
    follower_count = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
        'user',
        'content',
        'follower_count',
        ]

    def get_follower_count(self,obj):
        return 0
