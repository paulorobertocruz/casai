from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length = 50, unique = True)
    sigla = models.CharField(max_length = 2)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return "{0}/{1}".format(self.nome, self.sigla)

class Cidade(models.Model):
    nome = models.CharField(max_length = 255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


    def __str__(self):
        return "{0}/{1}".format(self.nome, self.estado.sigla)

class Endereco(models.Model):
    nome = models.CharField(max_length = 255)
    descricao = models.TextField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    cep = models.CharField(max_length = 255)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return "{0}/{1}".format(self.nome, self.cidade)

class Distrito(models.Model):
    nome = models.CharField(max_length = 255)

    class Meta:
        verbose_name = "Distrito"
        verbose_name_plural = "Distritos"


    def __str__(self):
        return "DSEI: {0}".format(self.nome)

class Polo(models.Model):
    nome = models.CharField(max_length = 255)
    distrito = models.ForeignKey(Distrito, on_delete=models.SET_NULL, null = True)

    class Meta:
        verbose_name = "Polo"
        verbose_name_plural = "Polos"


    def __str__(self):
        return "POLO: {0} - {1}".format(self.nome, self.distrito)

class Etnia(models.Model):
    nome = models.CharField(max_length = 255)

    class Meta:
        verbose_name = "Etnia"
        verbose_name_plural = "Etnias"


    def __str__(self):
        return "{0}".format(self.nome)

class Aldeia(models.Model):
    nome = models.CharField(max_length = 255)
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
    polo = models.ForeignKey(Polo, on_delete=models.SET_NULL, null = True)

    class Meta:
        verbose_name = "Aldeia"
        verbose_name_plural = "Aldeias"


    def __str__(self):
        return "{0} - {1}".format(self.nome, self.polo)

ESTADO_CIVIL_CHOICES = ( ("CASADO", "CASADO"), ("SOLTEIRO", "SOLTEIRO"), ("DIVORCIADO", "DIVORCIADO"), ("VIUVO", "VIUVO") )
SEXO_CHOICES = ( ("M", "M"), ("F", "F") )

class Usuario(models.Model):
    nome = models.CharField(max_length = 255)
    nome_mae = models.CharField(max_length = 255)
    nome_pai = models.CharField(max_length = 255, null = True, blank = True)

    data_nascimento = models.DateField()
    sexo = models.CharField(max_length = 10, choices = SEXO_CHOICES)

    rg = models.CharField(max_length = 255, null = True, blank = True)
    cpf = models.CharField(max_length = 255, null = True, blank = True)
    cartao_sus = models.CharField(max_length = 100, null = True, blank = True)

    estado_civil = models.CharField(max_length = 20, choices = ESTADO_CIVIL_CHOICES, null = True, blank = True )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


    def __str__(self):
        return "{0} - mae: {1} ".format(self.nome, self.nome_mae)

    

class Prontuario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    numero = models.IntegerField()
    caixa = models.IntegerField()

    class Meta:
        verbose_name = "Prontuario"
        verbose_name_plural = "Prontuarios"


    def __str__(self):
        return "{0}/{1}/{2}".format(self.usuario, self.numero, self.caixa)

class UsuarioAldeiado(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.usuario, self.aldeia)

class EtniaUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0} - {1}".format(self.usuario, self.etnia)

    class Meta:
        unique_together = ("usuario", "etnia")

