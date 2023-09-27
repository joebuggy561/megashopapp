from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField()
    phone_number = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.first_name
# Create your models here.
