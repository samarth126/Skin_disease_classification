from django.db import models

# Create your models here.

class Dataset(models.Model):
    disease_image = models.ImageField(null=True, blank=True, upload_to="images/")
    disease_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.disease_name

class img_check(models.Model):
    disease_image = models.ImageField(null=True, blank=True, upload_to="image_check/")
    disease_name = models.CharField(max_length=200)

    def __str__(self):
        return self.disease_name

