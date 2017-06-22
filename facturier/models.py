# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    archive = models.ForeignKey('Archive', related_name='archive')
    devis = models.ForeignKey('Devis')

class Devis(models.Model):
    date = models.DateTimeField()
    price = models.FloatField()
    statut = models.ForeignKey('Statut')

class Statut(models.Model):
    en_cours = models.CharField(max_length=20)
    facture = models.CharField(max_length=20)
    annulee = models.CharField(max_length=20)

class Archive(models.Model):
    user = models.ForeignKey('User', related_name='username')
    devis = models.ForeignKey('Devis')
