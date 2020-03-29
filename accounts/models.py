from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.
class Customer(models.Model):
    full_name   = models.CharField(max_length = 50);
    mob_no      = models.CharField(max_length = 10);
    last_active = models.DateTimeField(auto_now = True);
    created     = models.DateTimeField(auto_now_add = True);
    city        = models.CharField(max_length = 30);
    colony      = models.CharField(max_length = 100);
    location    = PlainLocationField(based_fields=['city'], zoom=7);
    
    
    _verified = False;
    
    def  __str__(self):
        return self.full_name;
    def isVerified(self):
        return self._verified;
    def setVerified(self,status):
        self._verified = status;
        
        
class VerifiedCustomer(models.Model):
    full_name   = models.CharField(max_length = 50);
    mob_no      = models.CharField(max_length = 10);
    last_active = models.DateTimeField(auto_now = True);
    customer_id = models.IntegerField();
    
    def  __str__(self):
        return self.full_name;

   
    
