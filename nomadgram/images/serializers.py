from rest_framework import serializers
from nomadgram.users import models as user_models
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from . import models

class SmallImageSerializer(serializers.ModelSerializer):

    '''Used for the notifications '''

    class Meta:
        model = models.Image
        fields = (
            'file',
        )


class CountImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count'

        )

class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count'
        )

class CommentSerializer(serializers.ModelSerializer):


    creator = FeedUserSerializer(read_only=True)

    #image = ImageSerializer()

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )


class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'locations',
            'caption',
            'comments',
            'like_count',
            'creator',
            'tags',
            'created_at'

        )


class LikeSerializer(serializers.ModelSerializer):

    #image = ImageSerializer()

    class Meta:
        model = models.Like
        fields = '__all__'


class InputImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'file',
            'locations',
            'caption',

        )








