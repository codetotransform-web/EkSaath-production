from django.urls import path
from . import views



urlpatterns = [
    path('verify_mob_no/', views.verify_mob_no_view,name='verify_mob_no_customer'),
    path('login/<mob_no>', views.login_view,name='login'),
    path('register/<mob_no>',views.register_view,name='register'),
    path('register/fill_details/<mob_no>',views.fill_details_view,name="customer_details"),
    path('logout/<int:id>',views.logout_view,name='logout'),
]
