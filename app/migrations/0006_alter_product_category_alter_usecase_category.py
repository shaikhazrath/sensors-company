# Generated by Django 4.1.5 on 2023-02-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_category_alter_usecase_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('E', 'environmental monitoring'), ('S', 'signal conversion'), ('N', 'network'), ('T', 'Temperature monitoring')], max_length=50),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='category',
            field=models.CharField(choices=[('F', 'Food'), ('SF', 'Smart Farm'), ('FM', 'Facility management'), ('PM', 'Precision machine'), ('EL', 'Electronics industry'), ('WT', 'Water treatment'), ('O', 'Oem'), ('PB', 'Pharmaceutical Bio')], max_length=50),
        ),
    ]
