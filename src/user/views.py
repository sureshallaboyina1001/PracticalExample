from django.shortcuts import render,redirect
from .models import LoginSystem,LoginTime
import pygeoip
import socket


def index(request):
    return render(request,'index.html',{})


def register(request):
    if "submit" in request.POST:
        form_data = request.POST.get
        username = form_data('username')
        email = form_data('email')
        confirm_email = form_data('confirm_email')
        confirm_password = form_data('confirm_password')
        GEOIP=pygeoip.GeoIP("user/GeoIP.dat",pygeoip.MEMORY_CACHE)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip=s.getsockname()[0]
        country=GEOIP.country_name_by_addr(ip)
        print(country)
        password = form_data('password')
        obj=LoginSystem.objects.create(username=username,email=email,password=password,user_location=country,confirm_email=confirm_email,confirm_password=confirm_password)
        if obj:
            return redirect('/')
    return render(request,'register.html',{})
    s.close()

def login(request):
    if "login" in request.POST:
         form_data = request.POST.get
         email = form_data('email')
         password = form_data('password')
         request.session['email']=email
         request.session['password']=password
         obj=LoginSystem.objects.filter(email=email,password=password)
         if obj:
             id=obj.values('id')
             print(id)
             store = LoginTime.objects.create(login_id=list(id)[0]["id"])
             if store:
                 return redirect('/')


    return render(request,'login.html',{})
