from django.db import models

from identidade.models import Usuario, Endereco
from django.db import models


class UnidadeDeSaude(models.Model):
    nome = models.CharField(max_length = 255)

    def __str__(self):
        return "{0}".format(self.nome)

class Fluxo(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    tipo = models.CharField(choices = ( ("PACIENTE", "PACIENTE"), ("ACOMPANHANTE", "ACOMPANHANTE"), ("TRANSITO", "TRANSITO") ), max_length = 20)

    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField(null = True, blank = True)

    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} - {1} - Entrada: {2}".format(self.tipo, self.usuario, self.data_entrada)

    def usuario__nome(self):
        return self.usuario.nome

    def usuario__nome_mae(self):
        return self.usuario.nome_mae


class Acompanhate(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fluxo = models.ForeignKey(Fluxo, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} => {1}".format(self.usuario, self.fluxo)


class EspecialidadeMedica(models.Model):
    nome = models.CharField(max_length = 255)
    subespecialidade_de = models.ForeignKey("EspecialidadeMedica", null = True, blank = True)

    def __str__(self):
        if self.subespecialidade_de is not None:
            return "{0} - {1}".format(self.subespecialidade_de, self.nome)
        else:
            return "{0}".format(self.nome)

class Internacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    unidade_saude = models.ForeignKey(UnidadeDeSaude, on_delete=models.SET_NULL, null = True)
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField(null = True, blank = True)
    relatorio = models.TextField()

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.usuario, self.unidade_saude)

    class Meta:
        verbose_name = "Internação"
        verbose_name_plural = "Internações"


class EspecialidadeMedicaInternacao(models.Model):
    internacao = models.ForeignKey(Internacao, on_delete=models.CASCADE)
    especialidade_medica = models.ForeignKey(EspecialidadeMedica, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("internacao", "especialidade_medica")
    
TIPO_CONSULTA_CHOICES = ( ("EMERGENCIAL", "EMERGENCIAL"), ("AMBULATORIAL", "AMBULATORIAL"))

class Consulta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateTimeField()
    
    tipo = models.CharField(max_length = 50, choices = TIPO_CONSULTA_CHOICES)
    unidade_saude = models.ForeignKey(UnidadeDeSaude, on_delete=models.SET_NULL, null = True)
    especialidade = models.ForeignKey(EspecialidadeMedica, on_delete=models.SET_NULL, null = True)
    
    
    relatorio = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.usuario, self.unidade_saude)

class Hobito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    data = models.DateTimeField()
    relatorio = models.TextField()

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.usuario, self.data)
    
class Encaminhamento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(EspecialidadeMedica, on_delete=models.SET_NULL, null = True)
    relatorio = models.TextField()

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.usuario, self.especialidade, self.criado_em)


class Regulacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    encaminhamento = models.OneToOneField(Encaminhamento, on_delete=models.CASCADE)

    origem = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name="origem_set")
    destino = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name="destino_set")
    data = models.DateTimeField()
    
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1} => {2} - {3}".format(self.usuario, self.origem, self.destino, self.data)
