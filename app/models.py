from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
# Create your models here.

USECASE_CHOICES = {
('F', 'Food'),
('PB','Pharmaceutical Bio'),
('PM','Precision machine'),
('EL','Electronics industry'),
('FM','Facility management'),
('WT','Water treatment'),
('SF','Smart Farm'),
('O','Oem'),
}
class Usecase(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(choices=USECASE_CHOICES,max_length=50)
    image = CloudinaryField('electronics')


PRODUCTS_CHOICES = {
('N', 'network'),
('T', 'Temperature monitoring'),
('E', 'environmental monitoring'),
('S', 'signal conversion'),
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
