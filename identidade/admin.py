from django.contrib import admin

# Register your models here.

from . import models
from relatorios import models as relatorio_models

admin.site.register(models.Etnia)

class InlineProntuario(admin.StackedInline):
    model = models.Prontuario
    extra = 0

class InlineHobito(admin.StackedInline):
    model = relatorio_models.Obito
    extra = 0

class InlineUsuarioAldeiado(admin.StackedInline):
    model = models.UsuarioAldeiado
    extra = 0

class InlineEtniaUsuario(admin.StackedInline):
    model = models.EtniaUsuario
    extra = 0


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "nome_mae", "sexo", "data_nascimento")
    list_filter = ("sexo","etniausuario__etnia","usuarioaldeiado__aldeia__polo__distrito","usuarioaldeiado__aldeia__polo", "usuarioaldeiado__aldeia", "prontuario__numero")
    search_fields = ("nome", "nome_mae", )
    inlines = [InlineEtniaUsuario, InlineUsuarioAldeiado, InlineProntuario, InlineHobito, ]

admin.site.register(models.Usuario, UsuarioAdmin)

admin.site.register(models.Estado)
admin.site.register(models.Cidade)
admin.site.register(models.Endereco)

admin.site.register(models.Distrito)

class PoloAdmin(admin.ModelAdmin):
    list_filter = ("distrito", )

admin.site.register(models.Polo, PoloAdmin)

admin.site.register(models.Aldeia)


