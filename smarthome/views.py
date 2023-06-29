from django.shortcuts import render
from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages,auth
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from smarthome.models import Light, SecurityCamera, Speaker, Television, Thermostat
from twilio.rest import Client
from . import urls

TWILIO_SID = 'AC876f0ae8543e9b379945a308b6e13f95'
TWILIO_AUTH_TOKEN = '7e171d888c7da8273440ccae8186e7fc'
TWILIO_PHONE_NUMBER = '+15676667274'


def index(request):
     
     if request.method == "POST":
          u = request.POST.get('username')
          p = request.POST.get('password')
     
          person = authenticate(request,username=u,password=p)
      #    try:
          if person is not None:
                    login(request,person)





                    request.session['person_name'] = person.first_name
                    request.session['person_last_name'] = person.last_name
                    request.session['person_username'] = person.username
                    request.session['person_email'] = person.email



                    return redirect('dashboard')
          
                    
          else:
                error_message = "Invalid username or password."
                return render(request, 'index.html', {'error_message': error_message})
                
     
     return render(request,'index.html')



def dashboard(request):
        return render(request, "dashboard.html")


from .models import Light, Thermostat, Speaker, SecurityCamera, Television

def add_delete_device(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        device_name = request.POST.get('device_name')
        device_type = request.POST.get('device_type')

        if action == 'Add Device':
               if device_type == 'light':
                    light = Light(light_name=device_name)
                    light.save()
               elif device_type == 'thermostat':
                    thermostat = Thermostat(thermostat_name=device_name)
                    thermostat.save()
               elif device_type == 'speaker':
                    speaker = Speaker(speaker_name=device_name)
                    speaker.save()
               elif device_type == 'camera':
                    camera = SecurityCamera(camera_name=device_name)
                    camera.save()
               elif device_type == 'tv':
                    tv = Television(tv_name=device_name)
                    tv.save()

        elif action == 'Delete Device':
               if device_type == 'light':
                    Light.objects.filter(light_name=device_name).delete()
               elif device_type == 'thermostat':
                    Thermostat.objects.filter(thermostat_name=device_name).delete()
               elif device_type == 'speaker':
                    Speaker.objects.filter(speaker_name=device_name).delete()
               elif device_type == 'camera':
                    SecurityCamera.objects.filter(camera_name=device_name).delete()
               elif device_type == 'tv':
                    Television.objects.filter(tv_name=device_name).delete()
        else:
                 return render(request, 'dashboard.html')

               


        return redirect('dashboard')

def turn_on_lights(request):
    lights = Light.objects.all()

    for light in lights:
        light.status = True
        light.save()

    # send phone notification
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body='Lights have been turned on!',
        from_=TWILIO_PHONE_NUMBER,
        to='+40770592301'
    )

    return redirect('dashboard')









