from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Lead(models.Model):
  search_time = models.DateTimeField(default=datetime.now, blank=True)
  keywords = models.CharField(max_length=200, default="")
  city = models.CharField(max_length=100)
  bedrooms = models.IntegerField(default=1)
  state = models.CharField(max_length=100)
  price = models.IntegerField(default = 1000)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.city+" "+self.state

class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=4, decimal_places=1)
  bedrooms = models.IntegerField()
  bathrooms = models.IntegerField(default=0)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.IntegerField(default=0)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title