from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.UnidadeDeSaude)
admin.site.register(models.EspecialidadeMedica)

class InlineEspecialidadeMedicaInternacao(admin.StackedInline):
    model = models.EspecialidadeMedicaInternacao
    extra = 0

class InternacaoAdmin(admin.ModelAdmin):
    inlines = [InlineEspecialidadeMedicaInternacao]

admin.site.register(models.Internacao, InternacaoAdmin)

admin.site.register(models.Consulta)
admin.site.register(models.Encaminhamento)
admin.site.register(models.Obito)
admin.site.register(models.Regulacao)

class InlineAcompanhante(admin.StackedInline):
    model = models.Acompanhante
    extra = 0

class FluxoAdmin(admin.ModelAdmin):
    list_display = ("usuario__nome", "usuario__nome_mae", "tipo", "data_entrada", "data_saida")
    list_filter = ("tipo",)
    inlines = [InlineAcompanhante]

admin.site.register(models.Fluxo, FluxoAdmin)

admin.site.register(models.Acompanhante)