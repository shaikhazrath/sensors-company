# Generated by Django 4.1.5 on 2023-02-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('S', 'signal conversion'), ('T', 'Temperature monitoring'), ('N', 'network'), ('E', 'environmental monitoring')], max_length=50),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='category',
            field=models.CharField(choices=[('FM', 'Facility management'), ('F', 'Food'), ('O', 'Oem'), ('EL', 'Electronics industry'), ('PB', 'Pharmaceutical Bio'), ('SF', 'Smart Farm'), ('WT', 'Water treatment'), ('PM', 'Precision machine')], max_length=50),
        ),
    ]
