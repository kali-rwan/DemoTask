from django.db import models


# Create your models here
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    date_added= models.DateTimeField(auto_now_add=True)
    merchant = models.ForeignKey(merchant, on_delete=models.CASCADE,null=True)


class merchant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)