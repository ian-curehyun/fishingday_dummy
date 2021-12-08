from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FishingDayPost
from .serializers import FishingDayPostSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world")

@api_view(['GET'])
def randomPost(request, id):
    totalPosts = FishingDayPost.objects.all()
    randomPosts = random.sample(list(totalPosts), id)
    serializer = FishingDayPostSerializer(randomPosts, many=True)
    return Response(serializer.data)
