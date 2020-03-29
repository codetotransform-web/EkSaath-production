from django.db import models

# Create your models here.

class Uploader(models.Model):
    full_name   = models.CharField(max_length = 50);
    mob_no      = models.CharField(max_length = 10);
    last_active = models.DateTimeField(auto_now = True);
    created     = models.DateTimeField(auto_now_add = True);
    
    
    
    _verified = False;
    
    def  __str__(self):
        return self.full_name;
    def isVerified(self):
        return self._verified;
    def setVerified(self,status):
        self._verified = status;
        
        
class VerifiedUploader(models.Model):
    full_name   = models.CharField(max_length = 50);
    mob_no      = models.CharField(max_length = 10);
    last_active = models.DateTimeField(auto_now = True);
    uploader_id = models.IntegerField()
    
    def  __str__(self):
        return self.full_name;

        
class OTP: 
    
    def __init__(self,val):
        self.value = val;
    
    def set_otp(self,val):
        self.value = val;
    
    def get_otp(self):
        return self.value;
