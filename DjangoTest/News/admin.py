from django.contrib import admin
from News.models import *

# admin.site.register(News)
admin.site.register(NewsType)
admin.site.register(Editor)


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "time"]
    list_filter = ["title"]
    search_fields = ["title"]


admin.site.register(News, NewsAdmin)
# Register your models here.
