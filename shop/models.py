from django.db import models

# Create your models here.
class Products(models.Model):
	def __str__(self):
		return self.title
	title = models.CharField(max_length=200)
	price = models.IntegerField()
	discount_price = models.IntegerField()
	category = models.CharField(max_length=200)
	description = models.TextField()
	image = models.CharField(max_length=300)

	def get_savings(self):
		return self.price - self.discount_price

class Order(models.Model):
	items = models.CharField(max_length=1000)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	address = models.CharField(max_length=1000)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zipcode = models.IntegerField()
	total = models.IntegerField()