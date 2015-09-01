from django.db import models

class Comuna(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoFie

    nombre = models.TextField(blank=True, null=True)  # This field type is a gue

    reg = models.ForeignKey('Region', blank=True, null=True)
    prov = models.ForeignKey('Provincia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'

class Establecimiento(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoFie

    nombre = models.TextField(blank=True, null=True)  # This field type is a gue

    direccion = models.TextField(blank=True, null=True)  # This field type is a

    num_dir = models.TextField(blank=True, null=True)  # This field type is a gu

    telefono = models.TextField(blank=True, null=True)  # This field type is a g

    clase = models.TextField(blank=True, null=True)  # This field type is a gues

    web = models.TextField(blank=True, null=True)  # This field type is a guess.

    reg = models.ForeignKey('Region', blank=True, null=True)
    prov = models.ForeignKey('Provincia', blank=True, null=True)
    com = models.ForeignKey(Comuna, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'establecimiento'


class Provincia(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoFie

    nombre = models.TextField(blank=True, null=True)  # This field type is a gue

    reg = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'


class Region(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoFie

    nombre = models.TextField(blank=True, null=True)  # This field type is a gue


    class Meta:
        managed = False
        db_table = 'region'