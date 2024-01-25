from django.db import models

class NuevaOrden(models.Model):
    ordenid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    factura = models.CharField(max_length=3, choices=[("Si", "Si"), ("No", "No")])
    rfc = models.CharField(max_length=13, null=True, blank=True)
    recurrente = models.CharField(max_length=3, choices=[("Si", "Si"), ("No", "No")])
    volumen = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    numero_rastreo = models.CharField(max_length=255, null=True, blank=True)
    precio_factura = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descripcion_mercancia = models.CharField(max_length=255, blank=True)
    tiempo_almacenamiento = models.CharField(max_length=255, null=True, blank=True)
    servicios_combinados = models.CharField(max_length=255, blank=True, null=True,)
    punto_de_carga = models.CharField(max_length=255, blank=True, null=True,)
    punto_de_descarga = models.CharField(max_length=255, blank=True, null=True,)

    SERVICE_CHOICES = [
        ('Transporte', 'Transporte'),
        ('Almacenamiento', 'Almacenamiento'),
        ('Distribución', 'Distribución'),
        ('Combinación de servicios', 'Combinación de servicios'),
    ]

    service_type = models.CharField(
        max_length=255,
        choices=SERVICE_CHOICES,
    )
    def __str__(self):
        return self.nombre  
