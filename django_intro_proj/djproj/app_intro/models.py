from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artigo(models.Model):
    titulo = models.CharField('Título', max_length=50)  # campo  "varchar" de até 50 caracteres
    texto = models.TextField('Corpo')   # campo texto
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # def Chave Estrangeira para o Modelo User
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)  #  def campo ""datetime"
    data_pub = models.DateTimeField('Publicado em')