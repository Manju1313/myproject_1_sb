from django.db import models
import datetime
from django.conf import settings


# Create your models here.
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)



class person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    #slug = models.SlugField(max_length=200, db_index=True, unique = True)
    age      =models.PositiveIntegerField(null=True,blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    date      =models.DateField(null=True,blank=True)

    def __str__(self):
        return self.first_name

class issue(models.Model):
    person         =models.ForeignKey('person' ,on_delete=models.CASCADE,null=True,blank=True)
    issue_name     =models.CharField(max_length=20,null=True, blank=True)
    join_date      =models.DateField(null=True,blank=True)
    Discharge_date =models.DateField(null=True,blank=True)
    def __unicode__(self):
        return (self.person,self.issue_name)

    # def __str__(self):
    #     return self.issue_name
   

class car(models.Model):
    car_name = models.CharField(max_length=255)
    name = models.OneToOneField(
        person,
        on_delete=models.CASCADE,
    )
    car_model = models.CharField(max_length = 100)


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(person, related_name='groups')
    #members = models.OneToOneField(person,on_delete=models.CASCADE,)


    def products_list(self):
        return ', '.join([a.first_name for a in self.members.all()])


