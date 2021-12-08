from rest_framework import serializers
from .models import FishingDayPost

class FishingDayPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishingDayPost
        fields = ('userName','postText','follow','editDate','image','youtube','hashtag','fishimage','postLiked','commented','fishingCertification','commentedUser','likedUser','viewerCount','fishName','fishSize','fishGeo','fishingMethod','fishingbait','fishingDate')