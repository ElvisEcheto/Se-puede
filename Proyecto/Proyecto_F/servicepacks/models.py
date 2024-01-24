from django.db import models

class Servicepack(models.Model):
    image = models.ImageField(upload_to='static/servicepack_images', null=True)
    name = models.CharField(max_length=255)
    decription = models.CharField(max_length=255)
    price = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name