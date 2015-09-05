from django.contrib import admin

from .models import Region
from .models import Provincia
from .models import Comuna
from .models import Establecimiento
from .models import SignUp

class ProvinciaAdmin(admin.ModelAdmin):
		list_display = ('nombre', 'reg')

class ComunaAdmin(admin.ModelAdmin):
		list_display = ('nombre', 'reg', 'prov')
		search_fields = ('reg', 'prov')

class EstablecimientoAdmin(admin.ModelAdmin):
		list_display = ('nombre', 'direccion', 'telefono', 'clase')
		search_fields = ('nombre','direccion')

admin.site.register(Region)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Establecimiento, EstablecimientoAdmin)
admin.site.register(SignUp)
