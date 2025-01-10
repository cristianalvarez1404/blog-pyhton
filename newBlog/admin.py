from django.contrib import admin
from newBlog.models import Write 

# Register your models here.

class WriteAdmin(admin.ModelAdmin):
    list_display = ("title","user","created_at","updated_at")

admin.site.register(Write,WriteAdmin)