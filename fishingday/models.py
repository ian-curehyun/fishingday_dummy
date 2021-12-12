from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class FishingDayPost(models.Model):
    userName = models.CharField(max_length=20)
    postText = models.TextField(null=True, blank=True)
    follow = models.BooleanField(default=False)
    editDate = models.DateTimeField()
    image = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    hashtag = models.TextField(null=True, blank=True)
    fishimage = models.URLField(null=True, blank=True)
    postLiked = models.BooleanField(default=False)
    commented = models.BooleanField(default=False)
    fishingCertification = models.BooleanField(null=True, blank=True, default=False)
    commentedUser = ArrayField(models.TextField(),blank=True) 
    likedUser = ArrayField(models.TextField(),blank=True)
    viewerCount = models.IntegerField()
    fishName = models.CharField(max_length=50, null=True, blank=True)
    fishSize = models.FloatField(null=True, blank=True)
    fishGeo = ArrayField(models.TextField(), blank=True)
    fishingMethod = models.CharField(max_length=100, null=True, blank=True)
    fishingbait = models.CharField(max_length=100, null=True, blank=True)
    fishingDate = models.DateTimeField(null=True, blank=True)






#       String? userImage;
#   String? userName;
#   bool? follow;
#   String? editDate;
#   String? postText;
#   List<String>? image;
#   String? youtube;
#   List<String>? hashtag;
#   String? fishingImage;
#   bool? postLiked;
#   bool? commented;
#   int? likedCount;
#   int? commentedCount;
#   bool? fishingCertification;
#   List<String>? commentUser;
#   List<String>? likedUser;
#   int? viewerCount;
#   String? fishName;
#   double? fishSize;
#   String? fishGeo;
#   String? fishingMethod;
#   String? fishingBait;
#   String? fishingDate;
