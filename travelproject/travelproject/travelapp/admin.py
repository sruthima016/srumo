from django.contrib import admin
from . models import place
# Register your models here.
admin.site.register(place)
from . models import staff
admin.site.register(staff)