from django.contrib import admin
from .models import calLimit
from .models import Food
# Register your models here.

admin.site.register(Food)
admin.site.register(calLimit)