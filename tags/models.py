from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    #what tagged applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #generic relationship
    #Type (product, video, article)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #ID
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()
