# Generated by Django 3.2.9 on 2022-03-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='problem',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
