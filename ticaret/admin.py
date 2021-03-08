from django.contrib import admin
from .models import Listings
from .models import Destination
# Register your models here.
admin.site.register(Listings)
admin.site.register(Destination)