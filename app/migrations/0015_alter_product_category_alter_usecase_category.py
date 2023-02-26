# Generated by Django 4.1.7 on 2023-02-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_contact_phone_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('environmental_monitoring', 'environmental_monitoring'), ('network', 'network'), ('signal_conversion', 'signal_conversion'), ('Temperature_monitoring', 'Temperature_monitoring')], max_length=50),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='category',
            field=models.CharField(choices=[('smart_Farm', 'Smart_Farm'), ('oem', 'Oem'), ('precision_machine', 'Precision_machine'), ('pharmaceutical_Bio', 'Pharmaceutical_Bio'), ('facility_management', 'Facility_management'), ('electronics_industry', 'Electronics_industry'), ('food', 'Food'), ('water_treatment', 'Water_treatment')], max_length=50),
        ),
    ]