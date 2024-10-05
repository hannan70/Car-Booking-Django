from django.contrib import admin
from contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_filter = ("car_title", "city",)
    list_display = ("full_name", 'car_title', 'email', "mobile", "state", "customer_needs")
    search_fields = ("first_name", 'car_title', "email", "mobile")
    list_display_links = ("full_name", "car_title")


# Register your models here.
admin.site.register(Contact, ContactAdmin)