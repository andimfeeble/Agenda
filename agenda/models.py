from enum import unique
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=50)
    fone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, max_length=50)
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("agenda:detail", kwargs={"pk": self.pk})
