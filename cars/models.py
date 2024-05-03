from django.db import models


class CarModel(models.Model):
    image = models.ImageField(upload_to='cars-images', null=True)
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=255)
    info = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'
