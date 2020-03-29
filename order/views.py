from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import Customer
from home.models import Product
from .models import Cart,Unconfirmed_order , Order_details , Successfull_order ,Successfull_order_details

import json
# Create your views here.


#For twillio
from twilio.rest import Client
from django.conf import settings
from django_twilio.decorators import twilio_view

from upload.models import Uploader , VerifiedUploader ,OTP



delivery_charge = 10;
GST = 0.15;# 15%

def cart_view(request,id):
    customer = Customer.objects.get(id = id);
    carts = Cart.objects.filter(customer_id = id);
    cart_items = [];
    
    for cart in carts:
        if(cart.quantity > 0):
            cart_items.append(cart);
        
    print(cart_items);
    no_of_cart_items = len(cart_items);
    context = {
        "customer" : customer,
        # "products" : products,
        "cart_items"    : cart_items,
        "no_of_cart_items" : no_of_cart_items,
        
    }
    return render(request,'order/cart.html',context);



def set_cart_view(request):
    
    bag = request.GET['bag'];
    bag = json.loads(bag);
    
    for cust in bag :
        for t in bag[cust]:
            if(len(Cart.objects.filter(customer_id = cust,product_id=int(t[0])) ) > 0):
                #print(Cart.objects.filter(customer_id = cust,product_id=int(t[0]))[0].quantity);
                item = Cart.objects.filter(customer_id = cust,product_id=int(t[0]))[0];
                item.quantity = t[1];
                item.save();
            else:
                item = Cart(customer_id = cust,product_id = int(t[0]),quantity = t[1]);
                item.save();
            
            print("Saved");
    
    # print(bag[request.GET['customer_id']])
    # print("Hello" , request.GET['customer_id'],len(request.GET['bag']));
    return HttpResponse(True);




def del_cart_view(request):
    try:
        print(request.GET['customer_id'],request.GET['product_id']);
        cart_item = Cart.objects.filter(customer_id = request.GET['customer_id'],product_id = request.GET['product_id'] );
        cart_item.delete();
        
        return HttpResponse(True);
    except:
        return HttpResponse(False);
    
    
def unconfirmed_order_view(request,customer_id):
  
    order_items = Cart.objects.filter(customer_id = customer_id);
    customer = Customer.objects.filter(id = customer_id)[0];
    
    effective_product_price = 0;
    for item in order_items:
        unc_order = Unconfirmed_order.objects.filter(customer_id = customer.id,product_id = item.product_id);
        if(len(unc_order) < 1):
            order = Unconfirmed_order(customer_id = customer.id,product_id = item.product_id,quantity = item.quantity,delivery_city = customer.city,delivery_colony = customer.colony,delivery_location = customer.location);
            order.save();
        
        product = Product.objects.get(id = item.product_id);
        effective_product_price += product.price * item.quantity;
    # print(total_price);
    
    grand_total = float(effective_product_price) + float(effective_product_price)*GST + float(delivery_charge);
    
    context = {
            "order_items" : order_items,
            "customer"    : customer,
            "effective_product_price" : effective_product_price,
            "no_of_cart_items" : len(Cart.objects.filter(customer_id = customer_id)),
            "grand_total" : grand_total,
            "GST"  : GST,
            "delivery_charge" : delivery_charge,
        };
    
    return render(request,'order/unconfirmed_order.html',context); #order/unconfirmed_order.html


def address_for_order_view(request,customer_id):
    order_items = Cart.objects.filter(customer_id = customer_id);
    customer = Customer.objects.get(id = customer_id);
    
    
    effective_product_price = 0;
    product_str = "";
    for item in order_items:
        unc_order = Unconfirmed_order.objects.filter(customer_id = customer.id,product_id = item.product_id);
        if(len(unc_order) < 1):
            order = Unconfirmed_order(customer_id = customer.id,product_id = item.product_id,quantity = item.quantity,delivery_city = customer.city,delivery_colony = customer.colony,delivery_location = customer.location);
            order.save();
        
        product = Product.objects.get(id = item.product_id);
        product_str += str(product.id)+"+"+str(item.quantity)+" ";
        effective_product_price += product.price * item.quantity;
    # print(total_price);
    
    grand_total = float(effective_product_price) + float(effective_product_price)*GST + float(delivery_charge);
    
    
    if(len(Order_details.objects.filter(customer_id = customer_id)) > 0):
        pass;
    else:
        order1 = Order_details(customer_id = customer_id,products = product_str.strip(),
                               delivery_name = customer.full_name,
                               delivery_city = customer.city,
                               delivery_colony = customer.colony,
                               delivery_mob_no = customer.mob_no,
                               delivery_location = customer.location,
                               order_price   = grand_total,
                            #    order_id      = str(customer_id) + str(id),
                               )
        order1.save();
        order1.order_id = str(customer_id) + str(order1.id);
        order1.save();
    
    
    # Default Address
    # city = customer.city;
    # colony = customer.colony;
    # location = customer.location;
    
    order = Order_details.objects.get(customer_id = customer_id);
    delivery_name = order.delivery_name;
    delivery_city = order.delivery_city;
    delivery_colony = order.delivery_colony;
    delivery_mob_no = order.delivery_mob_no;
    order_price = order.order_price;
    
    
    context = {
            "customer" : customer,
            "effective_product_price" : effective_product_price,
            "no_of_cart_items" : len(Cart.objects.filter(customer_id = customer_id)),
            "grand_total" : order_price,
            "GST"  : GST,
            "delivery_charge" : delivery_charge,
            
            "delivery_name" : delivery_name,
            "delivery_city" : delivery_city,
            "delivery_colony" : delivery_colony,
            "delivery_mob_no" : delivery_mob_no,
            
        };
    
    return render(request,'order/order_address.html',context);



def edit_delivery_address(request,customer_id):
    customer = Customer.objects.get(id = customer_id);
    if(request.method == "POST"):
        
        delivery_name = request.POST["delivery_name"];
        delivery_mob_no = request.POST["delivery_mob_no"];
        delivery_city = request.POST["delivery_city"];
        delivery_colony = request.POST["delivery_colony"];
        
        order_items = Cart.objects.filter(customer_id = customer_id);
        
        effective_product_price = 0;
        for item in order_items:
            unc_order = Unconfirmed_order.objects.filter(customer_id = customer.id,product_id = item.product_id);
            if(len(unc_order) < 1):
                order = Unconfirmed_order(customer_id = customer.id,product_id = item.product_id,quantity = item.quantity,delivery_city = customer.city,delivery_colony = customer.colony,delivery_location = customer.location);
                order.save();
            
            product = Product.objects.get(id = item.product_id);
            effective_product_price += float(product.price) * item.quantity;
        # print(total_price);
    
        grand_total = float(effective_product_price) + float(effective_product_price)*GST + float(delivery_charge);
        
        order = Order_details.objects.get(customer_id = customer_id); 
        order.delivery_name = delivery_name;
        order.delivery_mob_no = delivery_mob_no;
        order.delivery_city = delivery_city;
        order.delivery_colony = delivery_colony;
        order.save();
        
        
        return redirect("address_for_order",customer_id = customer_id);
        # context = {
        #     "customer" : customer,
        #     "effective_product_price" : effective_product_price,
        #     "no_of_cart_items" : len(Cart.objects.filter(customer_id = customer_id)),
        #     "grand_total" : grand_total,
        #     "GST"  : GST,
        #     "delivery_charge" : delivery_charge,
            
        #     "delivery_name"   : delivery_name,
        #     "delivery_mob_no" : delivery_mob_no,
        #     "delivery_city"   : delivery_city,
        #     "delivery_colony" : delivery_colony,
            
        # }
        
        # return render(request,'order/edited_delivery_address.html',context);

        
    else:
        order = Order_details.objects.get(customer_id = customer_id);
        delivery_name = order.delivery_name;
        delivery_city = order.delivery_city;
        delivery_colony = order.delivery_colony;
        delivery_mob_no = order.delivery_mob_no;
        order_price = order.order_price;
        

        
        context = {
            "customer" : customer,
            "no_of_cart_items" : len(Cart.objects.filter(customer_id = customer_id)),
            
            "delivery_name" : delivery_name,
            "delivery_city" : delivery_city,
            "delivery_colony" : delivery_colony,
            "delivery_mob_no" : delivery_mob_no,

        }
        return render(request,'order/edit_delivery_address.html',context);



otp = "";
@twilio_view
def order_view(request,customer_id):
    # Payment API inthis view
    
    
    if(request.method == "GET"):
        global otp;
        otp = OTP(123456);
        context = {
            "mob_no" : Customer.objects.get(id = customer_id).mob_no,
        };
        return render(request,'order/payment.html',context)
        
    else:
        if(str(otp.get_otp()) == str(request.POST["otp"])):
            customer = Customer.objects.get(id = customer_id);
            
            order = Order_details.objects.get(customer_id = customer_id);
            order_id = order.order_id;
            success_order = Successfull_order(  customer_id = customer_id,
                                                products = order.products,
                                                delivery_name = order.delivery_name,
                                                delivery_city = order.delivery_city,
                                                delivery_colony = order.delivery_colony,
                                                delivery_mob_no = order.delivery_mob_no,
                                                delivery_location = order.delivery_location,
                                                order_price   = order.order_price,
                                                order_id = order.order_id,
                               )
            success_order.save();
            
            
            products = [];
            products_list = success_order.products;
            products_list = products_list.split(" ");
            
            
            for product in products_list:
                ls = product.split("+");
                product_id = int(ls[0]);
                product_quantity = int(ls[1]);
                
                s_order_details = Successfull_order_details(customer_id = customer_id,
                        product_id = product_id,
                        quantity = product_quantity,
                        order_id = order.order_id,
                    );
                
                s_order_details.save();
            
            
            s_orders = Successfull_order_details.objects.filter(customer_id = customer_id);
            # Deleting data from the order buffer
            order.delete();
            # Deleting from the Cart
            cart_item = Cart.objects.filter(customer_id = customer_id);
            cart_item.delete();
            
            unc_order = Unconfirmed_order.objects.filter(customer_id = customer_id);
            unc_order.delete();
            
            
            context = {
                "customer" : customer,
                "order_id" : order_id,
                "s_orders"   : s_orders,
            }
            return render(request,'order/completed_order.html',context);
            
            
        else:
            error_msg = "Incorrect Otp";
            context = {
                # "mob_no":mob_no,
                "mob_no" : Customer.objects.get(id = customer_id).mob_no,
                "msg" : error_msg,
            }
            return render(request,'order/payment.html',context);
    
    






