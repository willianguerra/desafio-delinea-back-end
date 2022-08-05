from django.db import models
from uuid import uuid4

# Create your models here.

def upload_image_products(instance, filename):
    return f"{instance.id_product}-{filename}"

class Products(models.Model):
    id_product = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    responsible = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    creation = models.DateField(auto_now_add=True)
    price = models.FloatField()
    image = models.TextField(blank=True)