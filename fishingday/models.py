from django.db import models

# Create your models here.
class FishingDayPost(models.Model):
    userName = models.CharField(max_length=20)
    postText = models.TextField(null=True, blank=True)
    follow = models.BooleanField()
    editDate = models.DateTimeField()
    image = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    hashtag = models.TextField()
    fishimage = models.URLField(null=True, blank=True)
    postLiked = models.BooleanField()
    commented = models.BooleanField()
    fishingCertification = models.BooleanField(null=True, blank=True)
    commentedUser = models.TextField(null=True, default= 0)
    likedUser = models.TextField(null=True, default= 0)
    viewerCount = models.IntegerField()
    fishName = models.CharField(max_length=50, null=True, blank=True)
    fishSize = models.FloatField(null=True, blank=True)
    fishGeo = models.TextField(null=True, blank=True)
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
