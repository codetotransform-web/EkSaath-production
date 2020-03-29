from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:id>',views.upload_view,name="upload"),
    path('anonymous/',views.upload_anonymous_view,name="upload_anonymous"),
    path('uploads/<int:id>',views.upload_list_view,name="upload_list"),
    path('verify_mob_no/', views.verify_mob_no_view,name="verify_mob_no"),
    path('login/<mob_no>', views.uploader_login_view,name="uploader_login"),
    path('register/<mob_no>', views.uploader_register_view,name="uploader_register"),
    path('register/fill_details/<mob_no>',views.uploader_fill_details_view,name="uploader_details"),
    path('logout/<int:id>', views.uploader_logout_view,name="uploader_logout"),
    
]
