from django.db import models

# Create your models here.
class Good(models.Model):
	name = models.CharField(max_length=128)

class Category(models.Model):
	name = models.CharField(max_length=128)

class Shop（models.Model):
	name = models.CharField(max_length=128)


