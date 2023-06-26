from django.db import models
from django.core.validators import MinValueValidator

class PositiveDecimalField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [MinValueValidator(0)]
        super().__init__(*args, **kwargs)
