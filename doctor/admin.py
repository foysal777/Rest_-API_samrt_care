from django.contrib import admin
from .models import Doctor,Designation,Specialization,AvailableTime,Review
# Register your models here.
admin.site.register(Doctor)

class SpcializalizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {  'slug' : ('name',),}
    
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {  'slug' : ('name',),}
 
   
admin.site.register(Specialization , SpcializalizationAdmin)

admin.site.register(Designation,DesignationAdmin)
    
admin.site.register(AvailableTime)
admin.site.register(Review)