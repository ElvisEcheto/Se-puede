from django.db import models

class typelodging(models.Model):
    image = models.ImageField(upload_to='static/typelodging_images', null=True)
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
