from django.contrib import admin
from .models import post

# Register your models here.
#registering teh posts to be shown in the admin site
admin.site.register(post)
