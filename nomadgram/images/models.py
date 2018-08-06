from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from nomadgram.users import models as user_models



class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampedModel):

   
    file = models.ImageField()
    locations = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True, related_name='images')
    


    def __str__(self):
        return '{} - {}'.format(self.locations, self.caption)


class Comment(TimeStampedModel):

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='comments')
    

    def __str__(self):
        return self.message

class Like(TimeStampedModel):

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='likes')
    
    def __str__(self):
        return 'User: {} -Image Caption: {}'.format(self.creator.username, self.image.caption)
