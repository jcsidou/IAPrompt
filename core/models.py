from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass

class Model(models.Model):
    model_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class Prompt(models.Model):
    prompt_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)
    modelo = models.ForeignKey(Model, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    prompt = models.TextField(null=True, blank=True)
    json = models.FileField(upload_to='json_files/', null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, blank=True)

    def __str__(self):
        return self.descricao

    def average_rating(self):
        avg_rating = self.avaliacao_set.aggregate(models.Avg('nota'))['nota__avg']
        return round(avg_rating or 0, 1)  # Arredondando para 1 decimal

    def user_rating(self, user):
        avaliacao = self.avaliacao_set.filter(user=user).first()
        return avaliacao.nota if avaliacao else 0

class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    nota = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.prompt.descricao} - {self.nota}"
