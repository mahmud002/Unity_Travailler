from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Member)
admin.site.register(EventImage)

