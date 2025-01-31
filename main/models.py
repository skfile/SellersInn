from django.db import models
from django.utils import timezone


class userForm(models.Model):

    First_Name = models.CharField(max_length=200, null=True)
    Last_Name = models.CharField(
        max_length=200, null=True)

    Seller_Name = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=400, null=True)
    Zip_Code = models.CharField(max_length=200, null=True)

    Product_Name = models.CharField(max_length=1000, null=True)
    Product_Link = models.CharField(max_length=2500, null=True)

    def __str__(self):
        return self.Seller_Name


class newsletter(models.Model):
    Email = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.Email


class contact(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=400, null=True)
    Question = models.TextField()

    def __str__(self):
        return self.Name
