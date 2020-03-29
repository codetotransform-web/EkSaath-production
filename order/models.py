from django.db import models
from accounts.models import Customer
from home.models import Product
from location_field.models.plain import PlainLocationField

import random;

# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE);
    product  = models.ForeignKey(Product,on_delete = models.SET_NULL,null = True);
    quantity = models.IntegerField(default = 1);
    
    added_tocart_date = models.DateTimeField(auto_now = True);
    
    
    def __str__(self):
        return (str(self.customer) + str(self.product));
    


def get_order_id(k,l):
    return k+l;
       
class Unconfirmed_order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE);
    product  = models.ForeignKey(Product,on_delete = models.SET_NULL,null = True);
    quantity = models.IntegerField(default = 1);
    
    
    
    added_to_order_date = models.DateTimeField(auto_now = True);
    
    
    
class Order_details(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE);
    products = models.CharField(max_length = 1000);
    
    delivery_name = models.CharField(max_length = 50);
    delivery_city = models.CharField(max_length = 50);
    delivery_colony = models.CharField(max_length = 100);
    delivery_mob_no = models.CharField(max_length = 10,null=True);
    delivery_location   = PlainLocationField(based_fields=['delivery_city'], zoom=7,null = True);
    
    order_price = models.DecimalField(max_digits = 5,decimal_places = 2,null=True);
    
    order_date = models.DateTimeField(auto_now = True);
    
    order_id = models.CharField(max_length = 30);
    

class Successfull_order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE);
    products = models.CharField(max_length = 1000);
    
    delivery_name = models.CharField(max_length = 50);
    delivery_city = models.CharField(max_length = 50);
    delivery_colony = models.CharField(max_length = 100);
    delivery_mob_no = models.CharField(max_length = 10,null=True);
    delivery_location   = PlainLocationField(based_fields=['delivery_city'], zoom=7,null = True);
    
    order_price = models.DecimalField(max_digits = 5,decimal_places = 2,null=True);
    
    order_date = models.DateTimeField(auto_now = True);
    
    order_id = models.CharField(max_length = 30);
    delivered = models.BooleanField(default = False);
    

# Contains quantity for each product
class Successfull_order_details(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT);
    product  = models.ForeignKey(Product,on_delete = models.PROTECT,null = True);
    quantity = models.IntegerField(default = 1);
    
    order_date = models.DateTimeField(auto_now = True);
    
    delivered = models.BooleanField(default = False);
    
    order_id = models.CharField(max_length = 30,null = True);
    
    def __str__(self):
        return (str(self.customer) + str(self.product));