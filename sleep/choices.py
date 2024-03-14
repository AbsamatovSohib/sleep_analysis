from django.db import models


MY_SLEEP_CHOICES = (
    ("SLEEP_AID", "SLEEP AID"),
    ("SLEEP_SNORING",  "SLEEP & SNORING"),
    ("BREATHING_AIDS",  "BREATHING AIDS"),
    ("SLEEP_MASKS", "SLEEP MASKS"),
    ("LIVING_AIDS", "LIVING & SAFETY AIDS"),
    ("HERBAL_SUPPLEMENTS", "HERBAL_SUPPLEMENTS"),
    ("VITAMINS", "VITAMINS"),
)


class UserChoices(models.TextChoices):
    PREMIUM = "PREMIUM"
    NOT_PREMIUM = "NOT_PREMIUM"


class RatingChoices(models.TextChoices):
    ONE = "One"
    TWO = "two"
    THREE = "three"
    FOUR = "four"
    FIVE = "five"
