from django.contrib import admin
from .models import Produto, Cliente

# Para aparecer em tabelas
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)