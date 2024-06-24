from django.db import models


class IP(models.Model):
    ip = models.CharField(max_length=100, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(null=True, blank=True)
    label = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.ip

    class Meta:
        db_table = 'ip'
