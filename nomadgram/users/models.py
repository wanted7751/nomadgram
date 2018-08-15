from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class User(AbstractUser):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )

# name = CharField(_("Name of User"), blank=True, max_length=255)

    profile_image = models.ImageField(null=True, blank=True)
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    # A가 B를 팔로잉을 하면 B의 팔로워가 되어야 
    # 하는데 B의 프로필을 보면 같은 팔로잉이 되어있는 상황  symmetrical=False,  related_name="user"
    # 이와같이 해결해야하는 것 같음. 

    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username

    @property
    def post_count(self):
        return self.images.all().count()

        
    @property
    def followers_count(self):
        return self.followers.all().count()


    @property
    def following_count(self):
        return self.following.all().count()
