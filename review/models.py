from django.db import models
from django.conf import settings


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=100)
    body = models.TextField(null=True)
    #image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)
    region = models.ForeignKey(
        "commons.Region", related_name="reivews", null=True, on_delete=models.CASCADE)
    activity = models.ForeignKey(
        "commons.Activity", related_name="reivews", null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    body = models.CharField(null=True)
    
class Image(models.Model):
    review = models.ForeignKey(Review, null=True, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/', null=True, max_length=None, blank=True)
