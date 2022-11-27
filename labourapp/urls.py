from django.contrib import admin
from django.urls import path
from labourapp import views
urlpatterns = [
    path('', views.home,name="Home"),
    path('register', views.register,name="Register"),
    path('login', views.login,name="Login"),
    path('aboutus', views.aboutus,name="Aboutus"),
    path('contactus', views.contactus,name="Contactus"),
    path('formsubmit',views.formsubmit,name="formsubmit"),
    path('access',views.Access,name="access"),
    path('logout',views.Logout,name='logout')
    
]