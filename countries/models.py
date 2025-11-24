from django.db import models
from django.utils import timezone


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    poblacion = models.BigIntegerField()
    area = models.FloatField()
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # managers
    objects = ActiveManager()     # default manager: only non-deleted
    all_objects = models.Manager()  # includes deleted

    class Meta:
        db_table = 'paises'
        ordering = ['nombre']  # orden alfabético ascendente por defecto

    def __str__(self):
        return self.nombre

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'deleted_at'])

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save(update_fields=['is_deleted', 'deleted_at'])
