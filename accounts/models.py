from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    CHOICES = (("client", "Client"), ("manager", "Manager"))
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    avatar = models.ImageField(
        max_length=255, upload_to="media/avatars/", null=True, blank=True, default="/"
    )
    role = models.CharField(choices=CHOICES, max_length=20)
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )

    def __str__(self):
        return self.username
