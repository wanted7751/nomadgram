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
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")


    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
