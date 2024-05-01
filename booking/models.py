from django.db import models


class Profession(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Slots(models.Model):

    from_time = models.CharField(max_length=10)
    to_time = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)


# class Doctor(models.Model):
#     image = models.ImageField(upload_to="images/doctors/")
#     profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name="doctor_profession")
#     title = models.
