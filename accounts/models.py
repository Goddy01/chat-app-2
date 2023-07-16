from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

def user_profile_img_upload_location(instance, filename):
    return f'{instance.user.username}-{filename}'
class Profile(User):
    user =              models.OneToOneField(User, on_delete=models.CASCADE)
    full_name =         models.CharField(max_length=128)
    bio =               models.TextField(null=False)
    image =             models.ImageField(upload_to=user_profile_img_upload_location, default='default.jpg')
    website =           models.URLField(default='https://website.com/')
    facebook =          models.URLField(default='https://facebook.com/')
    twitter =           models.URLField(default='https://twitter.com/')
    instagram =         models.URLField(default='https://instagram.com/')

    def __str__(self):
        return f"{self.user.username}"
    
    def save(self, *args, **kwargs):
        """Overwrites the base save method"""
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300) # height, width
            img.thumbnail(output_size)
            img.save(self.image.path)