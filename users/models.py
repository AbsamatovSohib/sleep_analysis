from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from utils.choices import BloodGroup


class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    image = models.ImageField(upload_to='images/profile/', null=True,
                              default=None, blank=True)
    phone_number = models.CharField(max_length=7, null=True,
                                    default=None, blank=True)
    height = models.FloatField(null=True, default=None, blank=True)
    weight = models.FloatField(null=True, default=None, blank=True)
    blood_gr = models.CharField(max_length=4, choices=BloodGroup.choices,
                                default=None, null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(null=True, blank=True)

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
