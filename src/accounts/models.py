from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    homeaddress = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    experience = models.CharField(max_length=200)
    specialization = models.CharField(max_length=50)
    age = models.IntegerField()
    about = models.CharField(max_length=300)
    profile_pic = models.ImageField(null=True, blank=True)

    # def save(self):
    #     super().save()
    #     img = profile_pic.open(self.profile_pic.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_pic.path)

    def __str__(self):
        return self.user.username
