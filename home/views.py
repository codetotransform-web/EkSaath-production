from django.shortcuts import render,redirect
from .models import Category,Product
from accounts.models import Customer
from order.models import Cart



from twilio.rest import Client
from django.conf import settings

from django_twilio.decorators import twilio_view

# Create your views here.
def home_view(request):
    if(request.method == "POST"):
        pass;
    else:
        cats = Category.objects.all();
        context = {
                'categories':cats,
            };
        return render(request,'home.html',context);
    
    

def home_view_personal(request,id):
    cats = Category.objects.all();
    no_of_cart_items = len(Cart.objects.filter(customer_id = id));
    context = {
         "id":id,
         'categories':cats,
         "no_of_cart_items" : no_of_cart_items,
    }
    return render(request,'personal_home.html',context);
    # if(settings.CURRENT_USER.isVerified()):
    #     cats = Category.objects.all();
    #     context = {
    #         "user" : settings.CURRENT_USER,
    #         'categories':cats,
    #         "id" : settings.CURRENT_USER.id,
    #     }
    #     return render(request,'personal_home.html',context);
    # else:
    #     pass;
    # return render(request,'home.html',context);
    


def categories_view(request,category_id):
    if(request.method == "GET"):
        product_list = Product.objects.filter(category_id = category_id).order_by("name");
        
        context = {
            "product_list": product_list,
        }
        
        return render(request,'products.html',context);
    
def personal_categories_view(request,category_id,customer_id):
    
    if(request.method == "GET"):
        product_list = Product.objects.filter(category_id = category_id).order_by("name");
        no_of_cart_items = len(Cart.objects.filter(customer_id = customer_id));
        context = {
            "product_list": product_list,
            "id"          : customer_id,
            "no_of_cart_items" : no_of_cart_items,
        }
        
    return render(request,'products.html',context);
    
@twilio_view
def send_otp_view(request):
    
    message = 'This is DKB';
    to = '+918917350242';
    from_ = '+12018013748';
    
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	
    

    message = client.messages.create(body=message, to=to, from_=from_);
    print(message.sid);
    return redirect('home');



def dashboard_view(request,id):
   settings.CURRENT_USER = Customer.objects.filter(id = id)[0];
   user = settings.CURRENT_USER;
   context = {
        "user" : user,
        "id"   : id,
    }
   
   return render(request,'dashboard.html',context);














