from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(userForm)
admin.site.register(newsletter)
admin.site.register(contact)
