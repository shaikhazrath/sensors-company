# Generated by Django 4.1.5 on 2023-02-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_category_alter_usecase_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('T', 'Temperature monitoring'), ('S', 'signal conversion'), ('E', 'environmental monitoring'), ('N', 'network')], max_length=50),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='category',
            field=models.CharField(choices=[('F', 'Food'), ('FM', 'Facility management'), ('EL', 'Electronics industry'), ('SF', 'Smart Farm'), ('O', 'Oem'), ('PB', 'Pharmaceutical Bio'), ('WT', 'Water treatment'), ('PM', 'Precision machine')], max_length=50),
        ),
    ]
