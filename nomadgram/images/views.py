from django.shortcuts import render
from rest_framework.views import APIView
from . import models, serializers
from rest_framework.response import Response

# Create your views here.

class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:
            
            user_images = (following_user.images.all()[:2])

            for image in user_images:

                image_list.append(image)

        sorted_list = sorted(
            image_list, key=lambda image: image.created_at, reverse=True)

        print(sorted_list)

        serialzer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serialzer.data)

    
class LikeImage(APIView):
    
    def get(self, request, image_id, format=None):

        print(image_id)
    
        return Response(status=200)