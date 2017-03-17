from django.contrib import admin
from hello.models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','money','sex',)
    search_fields = ('name',)
    list_filter = ('name','sex','money',)
    ordering = ('name',)

# admin.site.register(Person)
admin.site.register(Person, PersonAdmin)
