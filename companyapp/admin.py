from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Company)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Website)
admin.site.register(Linkedin)
admin.site.register(Picupload)
admin.site.register(Whatsapp)
admin.site.register(Fax)
admin.site.register(Email)
