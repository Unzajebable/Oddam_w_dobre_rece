from django.db import models
from django.contrib.auth.models import User #email as username

ORG_CHOICE = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna")
)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    org_type = models.IntegerField(choices=ORG_CHOICE, default=1)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
