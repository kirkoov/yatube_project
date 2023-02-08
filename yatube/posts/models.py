from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    """Help the adin to add more topics for bloggers to post under."""
    # Group name
    title: models.CharField = models.CharField(max_length=30)
    # Group's unique address, part of its URL (e.g group/cats)
    slug: models.CharField = models.CharField(max_length=10)
    # Group description to highlight on the group homepage
    description: models.TextField = models.TextField()

    def __str__(self) -> str:
        """Return the group title."""
        return self.title


class Post(models.Model):
    """Help the admin manage posts in the database."""
    text: models.TextField = models.TextField()
    pub_date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    author: models.ForeignKey = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group: models.ForeignKey = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
