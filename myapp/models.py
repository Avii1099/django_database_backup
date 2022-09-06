from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=255)
    roll = models.PositiveIntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.name

