#from students.models import Dossier
#from courses.models import Address

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Dossier(models.Model):
    COICE_COLOR = (('r', 'red'), ('o', 'orange'), ('y', 'yellow)'))
    address = models.ForeignKey('courses.Address', models.SET_NULL, null = True)
    dislike_courses = models.ManyToManyField('courses.Course')
    like_colors = models.CharField(choices=COICE_COLOR, max_length=15)

class Coache(models.Model):
    ROLE_CHOICE = (('t', 'trener'), ('a', 'assistent'))
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, default='t')
    #course = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dossier = models.OneToOneField(Dossier, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return  str(self.name) + ' ' + str(self.surname) + '(' + str(self.role) + ')'

    def get_absolute_url(self):
        return reverse('coache_detail', kwargs={'pk': self.pk})
