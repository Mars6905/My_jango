from django.contrib import admin
from web_app.models import Laptop
@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('title',)

# Register your models here.
