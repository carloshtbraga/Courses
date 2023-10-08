from django.contrib import admin

# Register your models here.

from .models import Curso, Categoria, Instrutor, Carrinho, Pedido

admin.site.register(Curso)
admin.site.register(Categoria)
admin.site.register(Instrutor)
admin.site.register(Carrinho)
admin.site.register(Pedido)
