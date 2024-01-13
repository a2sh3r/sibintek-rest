from django.db import models


class Numbasum(models.Model):
    first_numba = models.DecimalField(default=0.0, decimal_places=2, max_digits=5, null=False, blank=False)
    second_numba = models.DecimalField(default=0.0, decimal_places=2, max_digits=5, null=False, blank=False)
    numba_sum = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
