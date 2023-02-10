# Generated by Django 4.1.5 on 2023-02-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_category_alter_usecase_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('S', 'signal conversion'), ('E', 'environmental monitoring'), ('N', 'network'), ('T', 'Temperature monitoring')], max_length=50),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='category',
            field=models.CharField(choices=[('SF', 'Smart Farm'), ('WT', 'Water treatment'), ('F', 'Food'), ('EL', 'Electronics industry'), ('PM', 'Precision machine'), ('FM', 'Facility management'), ('O', 'Oem'), ('PB', 'Pharmaceutical Bio')], max_length=50),
        ),
    ]