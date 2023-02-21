from django.db import models
from administration.choices import *
# Create your models here.

class residential_areas(models.Model):
  area_code = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=255, blank=True)

  class Meta:
        db_table = "residential_areas"
        
  def __str__(self):
      return self.name
    


class members(models.Model):
  names = models.CharField(max_length=255, null = True, blank=True)
  mbr_no = models.IntegerField(primary_key=True)
  id_no = models.IntegerField(blank=True, null=True)
  gender = models.CharField(null = True, blank=True, max_length=255, choices=GENDER_CHOICES)
  residential = models.ForeignKey(residential_areas, on_delete=models.DO_NOTHING, null=True, blank=True)
  phone_no = models.CharField(blank=True, null=True, max_length=255)
  next_of_kin = models.CharField(max_length=255, null=True, blank=True)
  phone_nos = models.CharField(blank=True, null=True, max_length=255)
  relationship = models.CharField(max_length=255, null = True, blank=True)
  image = models.ImageField(upload_to='members/passport_photo/', blank=True, null=True)
  
  class Meta:
        db_table = "members"
        
  def __str__(self):
      return self.names


