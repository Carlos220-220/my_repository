from django.contrib import admin
from Pet.models import *


class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Goods, PetAdmin)
admin.site.register(GoodsType)
admin.site.register(DogType)
# Register your models here.
