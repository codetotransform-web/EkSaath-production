from django.db import models
from upload.models import Uploader

# Create your models here.

def get_upload_path(instance,filename):
    return 'images/{}/{}'.format(instance.name,filename);

class Category(models.Model):
    name = models.CharField(max_length = 20);
    image = models.ImageField(upload_to = get_upload_path,blank=True);
    
    
    def __str__(self):
        return self.name;
    


def get_upload_path_for_product(instance,filename):
    # cat = Category.objects.filter(id = instance.category_id)(0).name;
    return 'images/{}/{}/{}/{}'.format(instance.category_id,instance.name,instance.quantity,filename);

class Product(models.Model):
    name = models.CharField(max_length = 50);
    category = models.ForeignKey(Category,on_delete = models.CASCADE);
    image = models.ImageField(upload_to = get_upload_path_for_product,blank=True);
    price = models.DecimalField(max_digits = 5,decimal_places = 2);
    quantity = models.CharField(max_length = 20);
    uploaded_by = models.ForeignKey(Uploader,on_delete = models.PROTECT,null=True);
    
	
                         
    
    def __str__(self):
        return self.name;
    def set_uploader(self,id):
        self.uploaded_by = id;
        return;