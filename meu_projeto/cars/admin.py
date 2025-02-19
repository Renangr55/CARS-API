from django.contrib import admin
from cars.models import Car, Brand

    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    


# Register your models here.
class CarAdmim(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year', 'value') # informando pro banco,cada tópico que é para aparecer
    search_fields = ('model', 'brand') # falando pro django que pode pesquisar model na barra de navegação do admin
    
    
   
admin.site.register(Car, CarAdmim) # reegistrando carro com modelo do car admim
admin.site.register(Brand, BrandAdmin)