from django.db import models

# Create your models here.

class Company(models.Model):
    name_company = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    create_at = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to="static/images", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return f"{self.name_company}"
    

class Car(models.Model):
    car_model = models.CharField(max_length=50)
    speed = models.IntegerField()
    color = models.CharField(max_length=50)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    probeg = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="static/images", height_field=None, width_field=None, max_length=None, null=True)
    def __str__(self):
        return f"{self.car_model}"
    

