from django.db import models


class Seccion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Secciones'


class Subseccion(models.Model):
    seccion= models.ForeignKey(Seccion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    class Meta:
        ordering = ['-nombre']
        verbose_name_plural = 'Subsecciones'

    def __str__(self):
        return self.nombre


class Ramo(models.Model):
    subseccion = models.ForeignKey(Subseccion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre

    def numero_evaluaciones(self):
        numero_evaluaciones = len(self.evaluaciones.all())
        return numero_evaluaciones


class TiposDeMaterial(models.Model):
    nombre = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Categorías de Evaluaciones'

class Evaluacion(models.Model):
    ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE, related_name="evaluaciones")
    tipo = models.ForeignKey(TiposDeMaterial, on_delete=models.CASCADE, null=True)
    anyo = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()
    archivo = models.FileField(null=True)

    def __str__(self):
        return self.archivo.name

    class Meta:
        ordering = ['-anyo']
        verbose_name_plural = 'Evaluaciones oficiales'

class Material(models.Model):

    ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE, related_name="materiales")
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=200, null=True)
    autor = models.CharField(max_length=50, null=True)
    archivo = models.FileField(null=True)

    def __str__(self):
        return '%s %s %s %s %s' % (self.ramo, self.nombre, self.descripcion, self.autor, self.archivo)

    class Meta:
        verbose_name_plural = 'Material complementario'


class BuscadorPatch(models.Model):

    ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE, related_name="patch_buscador")
    nombre_alternativo = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = 'Buscador Patches'

    def __str__(self):
        return '%s %s' % (self.nombre_alternativo, self.ramo.nombre)