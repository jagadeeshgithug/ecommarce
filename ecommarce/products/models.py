from django.db import models

# Create your models here.

class product_models(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images/",height_field=None,width_field=None)
    discription=models.CharField(max_length=200)
    cost=models.CharField(max_length=20)

    def __str__(self):
        return self.name