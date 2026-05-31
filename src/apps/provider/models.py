# src/apps/provider/models.py
from django.db import models
from apps.writer.models import TablaDatos

class TablaSnapshots(models.Model):
    id_snapshot = models.AutoField(primary_key=True)
    # Relación formal con el bloque original para rastrear el pasado
    id_dato = models.ForeignKey(
        TablaDatos, 
        on_delete=models.CASCADE, 
        db_column='id_dato'
    )
    vss_provider_usado = models.CharField(max_length=100, help_text="Ej: Software_Windows")
    contenido_congelado = models.TextField(help_text="Copia exacta al disparar VSS")
    fecha_captura = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tabla_snapshots'

    def __str__(self):
        return f"Snapshot {self.id_snapshot} (Dato Ref: {self.id_dato_id})"
