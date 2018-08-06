from django.shortcuts import render
from rest_framework.views import APIView
from . import models, serializers
from rest_framework.response import Response

# Create your views here.


class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)
