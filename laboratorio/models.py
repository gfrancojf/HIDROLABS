from django.db import models

class Muestra(models.Model):
    TIPOS_MUESTRA = (
        ('Agua potable', 'Agua potable'),
        ('Agua residual', 'Agua residual'),
        ('Agua de pozo', 'Agua de pozo'),
        # Agrega otros tipos de muestra según tus necesidades
    )
    cliente = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    fecha_toma_muestra = models.DateField()
    tipo_muestra = models.CharField(max_length=100, choices=TIPOS_MUESTRA)
    # Agrega otros campos relevantes para la muestra

class Analisis(models.Model):
    muestra = models.ForeignKey(Muestra, on_delete=models.CASCADE)
    fecha_analisis = models.DateField()
    # Campos para los parámetros de prueba
    turbiedad = models.FloatField()
    ph = models.FloatField()
    cloro = models.FloatField()
    # Agrega otros campos según tus necesidades

    def __str__(self):
        return f"Análisis para la muestra {self.muestra}"

class Resultado(models.Model):
    analisis = models.ForeignKey(Analisis, on_delete=models.CASCADE)
    parametro = models.CharField(max_length=100)
    valor = models.FloatField()
    unidad = models.CharField(max_length=50)
    # Agrega otros campos relevantes para el resultado

    def __str__(self):
        return f"Resultado del análisis {self.analisis} - {self.parametro}"

class Informe(models.Model):
    muestra = models.ForeignKey(Muestra, on_delete=models.CASCADE)
    # Agrega campos para la generación de informes