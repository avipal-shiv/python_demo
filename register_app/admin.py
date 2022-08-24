from django.contrib import admin


from register_app.models import *


from django.utils.html import format_html
from django.utils.safestring import mark_safe




class RegisterAdmin(admin.ModelAdmin):
    list_display = ('mobile','address')
    search_fields = ['user__mobile']    
   

admin.site.register(Register, RegisterAdmin)
