from django.shortcuts import render,HttpResponse,redirect
from labourapp.models import sub
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    return render (request, 'labour.html')
def register(request):
    return render (request, 'Register.html')
def login(request):
    if request.method=="POST":
       username=request.POST.get('username')
       password=request.POST.get('password')
       captcha=request.POST.get('captcha')
       newcaptcha1=request.POST.get('newcaptcha1')
      
       if captcha==newcaptcha1:
          user = authenticate(username=username, password=password)
          print("Working")
          if user is not None:
            auth.login(request,user)
            # A backend authenticated the credentials
            return redirect('/access')
          else:
            # No backend authenticated the credentials
           return redirect('/login')  
            
       else:
          print("Invalid Captcha")
         
    return render (request, 'Login.html')
def aboutus(request):
    alldata=sub.objects.all()
    data={
        'alldata':alldata
    }
    return render (request, 'About-us.html',data)
def contactus(request):
    return render (request, 'Contact-Us.html')
def formsubmit(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        street_name=request.POST.get('street_name')
        police_station=request.POST.get('police_station')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pin=request.POST.get('pin')
        work=request.POST.get('work')
        obj=sub(name=name,contact=contact,password=password,street_name=street_name,police_station=police_station,city=city,state=state,pin=pin,work=work)
        obj.save()
        n='You Have Registered Successfully..'
    return render (request, 'Register.html',{'n':n})
   
def Access(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render (request,'Access.html')
def Logout(request):
    logout(request)
    return redirect('/login')