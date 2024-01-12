import os
from uuid import uuid4

from django.db import models
from rest_framework.authtoken.admin import User

def path_to_rename(instance, filename):
    upload_to = 'cats_images'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}_{}.{}'.format(instance.pk, instance.product_name, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

class Cat(models.Model):
    class Hair(models.TextChoices):
        MAXIMUM = 'Maximum', 'Mega Volosataya'
        MEDIUM = 'Medium', 'Sredne Volosataya'
        LOW = 'Low', 'Korotkowerstnaya'
        BOLD = 'Bold', 'Lisaya'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cats', default=None)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    hair_style = models.CharField(max_length=7, choices=Hair.choices)
    cat_image = models.ImageField(default='default_cat.jpg', upload_to=path_to_rename)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.age}, {self.breed}, {self.hair_style}'
