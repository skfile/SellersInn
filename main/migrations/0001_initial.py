# Generated by Django 3.0.3 on 2020-08-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200, null=True)),
                ('Last_Name', models.CharField(max_length=200, null=True)),
                ('Email', models.CharField(max_length=400, null=True)),
                ('Seller_Name', models.CharField(max_length=200, null=True)),
                ('Zip_Code', models.CharField(max_length=200, null=True)),
                ('Product_Name', models.CharField(max_length=500, null=True)),
                ('Product_Link', models.CharField(max_length=2500, null=True)),
            ],
        ),
    ]
