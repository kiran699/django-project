from django.contrib import admin
from contactenquiry.models import contactEnquiry

class ServiceAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'phone', 'birthdate', 'gendermale', 'genderfemale', 'gendernone', 'address1', 'address2', 'place', 'city', 'postalcode')

admin.site.register(contactEnquiry, ServiceAdmin)

# Register your models here.

