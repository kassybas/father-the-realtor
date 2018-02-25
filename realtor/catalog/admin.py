from django.contrib import admin
from .models import Property, City, Heating, PropertyState, PropertyType

admin.site.register(Property)
admin.site.register(City)
admin.site.register(Heating)
admin.site.register(PropertyState)
admin.site.register(PropertyType)
# Register your models here.
