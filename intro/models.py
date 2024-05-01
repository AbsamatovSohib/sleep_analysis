from django.db import models
from utils.common import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Intro(BaseModel):
    title = models.CharField(max_length=127)
    image = models.ImageField(upload_to="images/intro/")


class Notifications(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_notifications")
    title = models.CharField(max_length=127)
    description = models.TextField()
    is_read = models.BooleanField(default=False)










