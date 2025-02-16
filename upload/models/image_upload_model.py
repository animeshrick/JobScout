from cloudinary.models import CloudinaryField
from django.db import models


class ImageUploadModel(models.Model):
    image = CloudinaryField("image", null=True, blank=True)
    public_id = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
