from django.db import models


class Todo(models.Model):
    feito = models.BooleanField(default=False)
    descricao = models.CharField(max_length=150)
    prazo = models.DateField()