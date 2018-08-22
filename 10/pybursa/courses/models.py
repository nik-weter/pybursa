from coaches.models import Coache

from django.db import models

# Create your models here.
class Address(models.Model):
    index = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    area = models.CharField(max_length=50)
    district = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.CharField(max_length=5)

class Course(models.Model):
    language = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    detail = models.TextField()
    slug = models.SlugField()
    prepod = models.ForeignKey(Coache, on_delete=models.SET_NULL, null=True)
    assistent = models.ForeignKey(Coache, on_delete=models.SET_NULL, blank=True, null=True,
related_name="course_assistant")
    start = models.DateField()
    end = models.DateField()
    venue = models.ForeignKey(Address, models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


