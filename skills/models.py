from django.db import models
from django.contrib.auth.models import User


# 💡 SKILL MODEL
class Skill(models.Model):

    CATEGORY_CHOICES = [

        ('coding', 'Coding'),

        ('design', 'Design'),

        ('editing', 'Editing'),

        ('teaching', 'Teaching'),

    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title


# 📂 RESOURCE MODEL
class Resource(models.Model):

    RESOURCE_TYPE = [

        ('demo', 'Demo'),

        ('premium', 'Premium'),

    ]

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='resources'
    )

    title = models.CharField(
        max_length=200
    )

    resource_type = models.CharField(
        max_length=20,
        choices=RESOURCE_TYPE
    )

    # optional link
    link = models.URLField(
        blank=True,
        null=True
    )

    # optional file
    file = models.FileField(
        upload_to='resources/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.skill.title} - {self.title}"