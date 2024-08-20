from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html("<img src='{}' width='40' style='border-radius: 3px;' />".format(object.car_image.url))

    thumbnail.short_description = "Photo"

    list_display = ('car_title', 'thumbnail', 'color', 'car_model', 'body_style', 'condition', 'is_featured')
    list_filter = ('car_title', 'color', 'year')
    search_fields = ('car_title', 'car_model', 'city', 'price',)
    list_editable = ("is_featured",)


admin.site.register(Car, CarAdmin)
