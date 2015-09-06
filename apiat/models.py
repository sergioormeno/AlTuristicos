from django.db import models


class Comuna(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoFie

    nombre = models.TextField(blank=True, null=True)  # This field type is a gue

    reg = models.ForeignKey('Region', blank=True, null=True)
    prov = models.ForeignKey('Provincia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'
    def __unicode__(self):
        return self.nombre

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
    def __unicode__(self):
        return self.nombre

class Provincia(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoFie

    nombre = models.TextField(blank=True, null=True)  # This field type is a gue

    reg = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'
    def __unicode__(self):
        return self.nombre

class Region(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoFie

    nombre = models.TextField(blank=True, null=True)  # This field type is a gue


    class Meta:
        managed = False
        db_table = 'region'
    def __unicode__(self):
        return self.nombre

class SignUp (models.Model):
    full_name = models.CharField(max_length=120, blank=True, null=True)

    email = models.EmailField()

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email


