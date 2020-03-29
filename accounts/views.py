from django.shortcuts import render,redirect,   get_object_or_404,redirect
from .forms import CustomerLoginForm , CustomerRegisterForm
from .models import Customer , VerifiedCustomer
from upload.models import OTP;
import random;


from twilio.rest import Client
from django.conf import settings
from django_twilio.decorators import twilio_view

# Create your views here.

otp = "";

def login_view(request,mob_no):
    
    
    if(request.method == "POST"):
        
        if(str(otp.get_otp()) == str(request.POST["otp"])):
            
            customer_id =  Customer.objects.get(mob_no = mob_no).id;
            
            current_customer = VerifiedCustomer.objects.create(
                mob_no = mob_no,
                full_name = Customer.objects.get(mob_no = mob_no).full_name,
                customer_id = customer_id,
            )
            current_customer.save();
            
            
            return redirect("home_personal",id=customer_id );
            # error_msg = "Incorrect Otp";
            # print("correct");
            # context = {
            #     "mob_no":mob_no,
            #     "msg" : error_msg,
            # }
            # return render(request,'upload/login.html',context);
            
        # print(otp[0],request.POST["otp"]);
        # if(str(otp[0]) == str(request.POST["otp"])):
        #     settings.CURRENT_USER.setVerified(True);
        #     return redirect('home_personal',id=settings.CURRENT_USER.id);
        # else:
        #     error_msg = "Incorrect Otp";
        #     context = {
        #         "msg" : error_msg,
        #     }
        #     return render(request,'accounts/login.html',context);
        
        
    
    else:
        context = {
            "mob_no":mob_no,    
        };
        return render(request,'accounts/login.html',context);
    
def register_view(request,mob_no):
    if(request.method == "POST"):
        if(str(otp.get_otp()) == str(request.POST["otp"])):
            
            
            try :
                
                    context = {
                        "mob_no":mob_no,
                        
                    }
                    # id = Uploader.objects.filter(mob_no = mob_no)[0].id;
                    print(str(otp.get_otp()),str(request.POST["otp"]));
                    return redirect("customer_details",mob_no = mob_no);
            except :
                    print("hello");
                    error_message = "Enter A valid Name";
                    context = {
                        "msg":error_message
                    }
                    form = CustomerRegisterForm({
                        'mob_no' : mob_no,
                    });
                    context = {
                        "form" : form,
                        'mob_no' : mob_no,
                    }
                    return render(request,"upload/register.html",context);
        else:
            error_message = "Incorrect OTP"
            form = CustomerRegisterForm({
                'mob_no' : mob_no,
                
            });
            context = {
                "form" : form,
                "mob_no":mob_no,
                "msg": error_message,
            }
            return render(request,"accounts/register.html",context);

    
    else:
        form = CustomerRegisterForm({
                'mob_no' : mob_no,
            });
        context = {
            "form" : form,
            "mob_no":mob_no,
        }
        return render(request,"accounts/register.html",context);

def fill_details_view(request,mob_no):
    if(request.method == "POST"):
        form = CustomerRegisterForm(request.POST);
        if(form.is_valid()):
            form.save();
            id = Customer.objects.filter(mob_no = mob_no)[0].id;
            return redirect("home_personal",id = id);
        else:
            error_message = "Enter a valid Name";
            form = CustomerRegisterForm({
                    'mob_no' : mob_no,
                });
            context = {
                        "form" : form,
                        "msg" : error_message,
                    }
            return render(request,"upload/register_details.html",context);
    
    else:
        form = CustomerRegisterForm({
                    'mob_no' : mob_no,
                });
        context = {
                    "form" : form,
                }
        return render(request,"accounts/register_details.html",context);

def logout_view(request,id):
    customer = VerifiedCustomer.objects.filter(customer_id = id);
    customer.delete();
    
    return redirect("home");
    
@twilio_view
def verify_mob_no_view(request):
    if(request.method == "POST"):
        form = CustomerLoginForm(request.POST);
        mob_no = request.POST["mob_no"];
        if(len(mob_no ) == 10 ):
            try:
                mob_no = int(mob_no);
                
                if(form.is_valid()):
                    
                    # user_exists = Customer.objects.filter(mob_no = mob_no);
                    global otp;
                    otp = OTP(123456); 
                    
                    
                    try : 
                        # Proceed to login 
                        uploader = get_object_or_404(Customer,mob_no=mob_no);
                        
                        
                        # Redirecting to Login Page
                        return redirect('login',mob_no = mob_no);
                        
                    except :
                        
                        # otp = OTP(123456);
                        # Proceed to Register
                        return redirect('register',mob_no = mob_no);
                    
                    # if(len(user_exists) > 0):
                    #     print(user_exists)
                    #     settings.CURRENT_USER = user_exists[0];
                        
                    #     # Send for otp verification
                    #     otp[0] = random.randint(100000,999999);
                        
                    #     mob_no = mob_no;
                    #     message = 'Hello '+str(mob_no)+"Your otp for EkSaath Account is : "+str(otp);
                    #     to = '+91'+str(mob_no);
                    #     from_ = '+12018013748';
                            
                    #     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                            
                            

                    #     message = client.messages.create(body=message, to=to, from_=from_);
                        
                        
                        
                        
                        
                    #     return redirect('login',mob_no = mob_no);
                    # else:
                    #     return redirect('register',mob_no = mob_no);
                        
            except:
                error_msg = "Enter a valid 10 digit Mobile Number";
                form = CustomerLoginForm();
            
                context = {
                    "form":form,
                    "msg" : error_msg,
                }
                return render(request,'accounts/verify_mob.html',context);
        
        else:
            error_msg = "Enter a valid 10 digit Mobile Number";
            form = CustomerLoginForm();
            
            context = {
                    "form":form,
                    "msg" : error_msg,
                };
            return render(request,'accounts/verify_mob.html',context);
    
        return redirect('verify_mob_no');
    else:
        form = CustomerLoginForm();
        
        context = {
            "form":form,
        };
        return render(request,'accounts/verify_mob.html',context);