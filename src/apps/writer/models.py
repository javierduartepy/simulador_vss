# src/apps/writer/models.py
from django.db import models
from apps.core.models import TablaVolumenes

class TablaDatos(models.Model):
    id_dato = models.AutoField(primary_key=True)
    # Relación formal con la infraestructura de volúmenes del Core
    id_volumen = models.ForeignKey(
        TablaVolumenes, 
        on_delete=models.CASCADE, 
        db_column='id_volumen'
    )
    ruta_archivo = models.CharField(max_length=255, help_text="Ej: /sistema/archivo1.bin")
    contenido_bloque = models.TextField(help_text="El valor del dato en producción")
    ultima_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tabla_datos'

    def __str__(self):
        return f"Dato {self.id_dato} - {self.ruta_archivo}"
