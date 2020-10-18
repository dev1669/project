from django.db import models

# Create your models here.
class Imagetest(models.Model):
    photo = models.ImageField(upload_to="pics")
    text = models.TextField(max_length=255,default="Automatic Slide")

    class Meta:
        verbose_name_plural = "Imagetest"

class Imagetext(models.Model):
    text = models.TextField(max_length=255,default="Automatic Slide")

    class Meta:
        verbose_name_plural = "Imagetext"

