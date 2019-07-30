from django.contrib import admin
from .models import Region, Activity, Subject

class RegionInline(admin.TabularInline):
  model = Region

class ActivityInline(admin.TabularInline):
  model = Activity

# Register your models here.
admin.site.register(Region)
admin.site.register(Activity)
admin.site.register(Subject)