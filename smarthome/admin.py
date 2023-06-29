from django.contrib import admin

from smarthome.models import Light, SecurityCamera, Speaker, Television, Thermostat

admin.site.register(Light)
admin.site.register(Thermostat)
admin.site.register(Speaker)
admin.site.register(SecurityCamera)
admin.site.register(Television)

