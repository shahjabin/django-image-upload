from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
# Create your models here.

MAX_SIZE_ALLOWED_IN_KB = 500;

def validate_size(imageFile):
    size = imageFile.file.size
    if size > 1024 * MAX_SIZE_ALLOWED_IN_KB:
        raise ValidationError(
            message= "Image file size should not exceed %(value)s KB",
            params= {
                "value": MAX_SIZE_ALLOWED_IN_KB
            },
            code= 123
        )    

class Photo(models.Model):
    image = models.ImageField(upload_to = "images", validators= [validate_size])
