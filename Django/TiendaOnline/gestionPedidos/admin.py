from django.contrib import admin

from gestionPedidos.models import Cliente

from gestionPedidos.models import Articulo

from gestionPedidos.models import Pedido  


class ClienteAdmin(admin.ModelAdmin):
	list_display=('nombre', 'direccion', 'tfono')
	search_fields=('nombre', 'tfono')

class ArticulosAdmin(admin.ModelAdmin):
	list_filter=('seccion',)

class PedidosAdmin(admin.ModelAdmin):
	list_display=('numero','fecha')
	list_filter=('fecha',)
	date_hierarchy='fecha'

admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Articulo, ArticulosAdmin)

admin.site.register(Pedido, PedidosAdmin)