from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
# Create your models here.

USECASE_CHOICES = {
('food', 'Food'),
('pharmaceutical_Bio','Pharmaceutical_Bio'),
('precision_machine','Precision_machine'),
('electronics_industry','Electronics_industry'),
('facility_management','Facility_management'),
('water_treatment','Water_treatment'),
('smart_Farm','Smart_Farm'),
('oem','Oem'),
}
class Usecase(models.Model):
    category = models.CharField(choices=USECASE_CHOICES,max_length=50)
    moredetails = HTMLField()



PRODUCTS_CHOICES = {
('network', 'network'),
('Temperature_monitoring', 'Temperature_monitoring'),
('environmental_monitoring', 'environmental_monitoring'),
('signal_conversion', 'signal_conversion'),
}
class Product(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=500)
    
    description = models.TextField()
    category = models.CharField(choices=PRODUCTS_CHOICES, max_length=50)
    tags = models.CharField(max_length=50)
    product_img1 = CloudinaryField('image')
    product_img2 = CloudinaryField('image')
    product_img3 = CloudinaryField('image')
    product_img4 = CloudinaryField('image')
    moredetails = HTMLField()

    def __str__(self):
        return str(self.title)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)