from django.contrib import admin
from .models import *

#registrando as models criadas na tela de admin do Django:

admin.site.register(Category)
admin.site.register(Company)

class adminMedicine(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_fk', 'company_fk')
    list_display_links = ('id', 'name',)
    search_fields = ('name','category_fk',)
    list_per_page = 10

admin.site.register(Medicine, adminMedicine)