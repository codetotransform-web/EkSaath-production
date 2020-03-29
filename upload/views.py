from django.shortcuts import render,redirect , get_object_or_404
from .models import Uploader , VerifiedUploader ,OTP
from home.models import Product
from .forms import UploaderRegisterForm , UploaderLoginForm , UploadForm 

# Create your views here.


#For twillio
from twilio.rest import Client
from django.conf import settings
from django_twilio.decorators import twilio_view

import random


otp = "";
@twilio_view
def verify_mob_no_view(request):
    if(request.method == "POST"):
        form = UploaderLoginForm(request.POST);
        mob_no = request.POST["mob_no"];
        
        if(len(mob_no ) == 10 and form.is_valid()):
            try : 
                    
                global otp;
                    # k = random.randint(100000,999999)
                    # otp = OTP(k);
                    # mob_no = mob_no;
                    # message = 'Hello '+str(mob_no)+"Your otp for EkSaath Account is : "+str(otp.get_otp());
                    # to = '+91'+str(7653960791);
                    # from_ = '+12018013748';
                                
                    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                    # message = client.messages.create(body=message, to=to, from_=from_);

                otp = OTP(123456);
                
                try : 
                    # Proceed to login 
                    uploader = get_object_or_404(Uploader,mob_no=mob_no);
                    
                    # otp = OTP(123456);
                    
                    # Redirecting to Login Page
                    return redirect('uploader_login',mob_no = mob_no);
                    
                except :
                    
                    # otp = OTP(123456);
                    # Proceed to Register
                    return redirect('uploader_register',mob_no = mob_no);
            except :
                    error_msg = "Enter a valid 10 digit Mobile Number";
                    form = UploaderLoginForm();
                
                    context = {
                        "form":form,
                        "msg" : error_msg,
                    }
                    return render(request,'accounts/verify_mob.html',context);
        
        else:
            error_msg = "Enter a valid 10 digit Mobile Number";
            form = UploaderLoginForm();
            
            context = {
                    "form":form,
                    "msg" : error_msg,
                };
            return render(request,'accounts/verify_mob.html',context);
    
        return redirect('verify_mob_no');                
                        
            # except:
            #     error_msg = "Enter a valid 10 digit Mobile Number";
            #     form = UploaderLoginForm();
            
            #     context = {
            #         "form":form,
            #         "msg" : error_msg,
            #     }
            #     return render(request,'accounts/verify_mob.html',context);
        
    
    
    else:
        form = UploaderLoginForm();
        
        context = {
            "form":form,
        };
        return render(request,'upload/verify_mob_no.html',context);
    
    
def uploader_login_view(request,mob_no):
    if(request.method == "POST"):
        if(str(otp.get_otp()) == str(request.POST["otp"])):
            
            uploader_id =  Uploader.objects.get(mob_no = mob_no).id;
            
            current_uploader = VerifiedUploader.objects.create(
                mob_no = mob_no,
                full_name = Uploader.objects.get(mob_no = mob_no).full_name,
                uploader_id = uploader_id,
            )
            
            
            return redirect("upload",id=uploader_id );
            # error_msg = "Incorrect Otp";
            # print("correct");
            # context = {
            #     "mob_no":mob_no,
            #     "msg" : error_msg,
            # }
            # return render(request,'upload/login.html',context);
            
        else:
            error_msg = "Incorrect Otp";
            context = {
                "mob_no":mob_no,
                "msg" : error_msg,
            }
            return render(request,'upload/login.html',context);
        
    else:
        context = {
            "mob_no":mob_no,
        }
        return render(request,'upload/login.html',context);

def uploader_register_view(request,mob_no):
    if(request.method == "POST"):
        if(str(otp.get_otp()) == str(request.POST["otp"])):
            
            try :
                
                    context = {
                        "mob_no":mob_no,
                        
                    }
                    # id = Uploader.objects.filter(mob_no = mob_no)[0].id;
                    return redirect("uploader_details",mob_no = mob_no);
            except :
                error_message = "Enter A valid Name";
                context = {
                    "msg":error_message
                }
                form = UploaderRegisterForm({
                    'mob_no' : mob_no,
                });
                context = {
                    "form" : form,
                    'mob_no' : mob_no,
                }
                return render(request,"upload/register.html",context);
        else:
            
            form = UploaderRegisterForm({
                'mob_no' : mob_no,
            });
            context = {
                "form" : form,
                "mob_no":mob_no,
            }
            return render(request,"upload/register.html",context);

    else:
        
        form = UploaderRegisterForm({
                'mob_no' : mob_no,
            });
        context = {
            "form" : form,
            "mob_no":mob_no,
        }
        return render(request,"upload/register.html",context);

def uploader_fill_details_view(request,mob_no):
    if(request.method == "POST"):
        form = UploaderRegisterForm(request.POST);
        if(form.is_valid()):
            form.save();
            id = Uploader.objects.filter(mob_no = mob_no)[0].id;
            return redirect("upload",id = id);
        else:
            error_message = "Enter a valid Name";
            form = UploaderRegisterForm({
                    'mob_no' : mob_no,
                });
            context = {
                        "form" : form,
                        "msg" : error_message,
                    }
            return render(request,"upload/register_details.html",context);
    
    else:
        form = UploaderRegisterForm({
                    'mob_no' : mob_no,
                });
        context = {
                    "form" : form,
                }
        return render(request,"upload/register_details.html",context);

def uploader_logout_view(request,id):
    
    uploader = VerifiedUploader.objects.filter(uploader_id = id);
    uploader.delete();
    
    return redirect("upload_anonymous");



def upload_anonymous_view(request):
    return render(request,"upload/anonymous.html");

def upload_view(request,id):
    if(request.method == "GET"):
        form = UploadForm({"uploaded_by" : id});
        context = {
            "id":id,
            "form" : form,
        }
        return render(request,"upload/home.html",context)
    
    # POST Request
    else :
        form = UploadForm(request.POST,request.FILES);
        if(form.is_valid()):
            form.save();
            
            return redirect("upload",id=id);
        else:
            context = {
                "id":id,
                "form" : form,
            }
            return render(request,"upload/home.html",context)
        context = {
            "id":id,
            "form" : form,
        }
        return render(request,"upload/home.html",context)
    
    
    
    
def upload_list_view(request,id):
    products = Product.objects.filter(uploaded_by = id);
    uploader = Uploader.objects.filter(id = id)[0];
    context = {
        "products" : products,
        "uploader" : uploader,
        "id" : id,
    }
    
    return render(request,'upload/upload_list.html',context);