from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInformation(models.Model):
    uid = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    roles = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

 #   def __str__(self):  # __unicode__ on Python 2
  #      return self.password


class PushData(models.Model):
    push_id = models.IntegerField(default=0)
    uid = models.CharField(max_length=200)
    month = models.CharField(max_length=200, default="")
    date_info = models.CharField(max_length=200, default="")


class CouponData(models.Model):
    uid = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    coupon_data = models.IntegerField(default=0)


class PresentInformation(models.Model):
    pres_id = models.IntegerField(default=0)
    pres_name = models.CharField(max_length=200)
    pres_number = models.IntegerField(default=0)


class ConvertData(models.Model):
    convert_id = models.IntegerField(default=0)
    uid = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    pres_id = models.ForeignKey(PresentInformation, on_delete=models.CASCADE)