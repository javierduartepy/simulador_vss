 # src/apps/service/models.py
from django.db import models

class TablaVolumenes(models.Model):
    id_volumen = models.AutoField(primary_key=True)
    letra_unidad = models.CharField(max_length=5, help_text="Ej: C:, D:")
    sistema_archivos = models.CharField(max_length=10, help_text="Ej: NTFS, ReFS")
    capacidad_total_gb = models.IntegerField()

    class Meta:
        db_table = 'tabla_volumenes'

    def __str__(self):
        return f"Volumen {self.letra_unidad} ({self.sistema_archivos})"

