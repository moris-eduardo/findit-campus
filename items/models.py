# items/models.py
from django.db import models
from django.conf import settings
import uuid


class CampusZone(models.Model):
    name        = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=255, blank=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'campus_zones'
        ordering = ['name']

    def __str__(self):
        return self.name


class Item(models.Model):

    class Category(models.TextChoices):
        ELECTRONICS  = 'ELECTRONICS',  'Electrónicos'
        CLOTHING     = 'CLOTHING',     'Ropa y calzado'
        ACCESSORIES  = 'ACCESSORIES',  'Mochilas y bolsas'
        DOCUMENTS    = 'DOCUMENTS',    'Documentos'
        KEYS         = 'KEYS',         'Llaves'
        GLASSES      = 'GLASSES',      'Lentes'
        SPORTS       = 'SPORTS',       'Artículos deportivos'
        BOOKS        = 'BOOKS',        'Libros y apuntes'
        JEWELRY      = 'JEWELRY',      'Joyería y accesorios'
        OTHER        = 'OTHER',        'Otro'

    class Color(models.TextChoices):
        BLACK      = 'BLACK',      'Negro'
        WHITE      = 'WHITE',      'Blanco'
        GRAY       = 'GRAY',       'Gris'
        BLUE       = 'BLUE',       'Azul'
        RED        = 'RED',        'Rojo'
        GREEN      = 'GREEN',      'Verde'
        YELLOW     = 'YELLOW',     'Amarillo'
        BROWN      = 'BROWN',      'Café / Marrón'
        PINK       = 'PINK',       'Rosa'
    