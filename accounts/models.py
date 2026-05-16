from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)

    skills_offered = models.TextField(blank=True)

    skills_needed = models.TextField(blank=True)

    # 📸 Profile image
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        default='default.png'
    )

    def __str__(self):
        return self.user.username