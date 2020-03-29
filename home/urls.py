from django.urls import path
from . import views



urlpatterns = [
    path('', views.home_view,name='home'),
    path('home/<int:id>/',views.home_view_personal,name="home_personal"),
    path('dashboard/<int:id>/', views.dashboard_view,name='dashboard'),
    path('categories/<int:category_id>/',views.categories_view,name='categories'),
    path('categories/<int:category_id>/<int:customer_id>',views.personal_categories_view,name='personal_categories'),
    path('otp/',views.send_otp_view,name='otp'),
]
