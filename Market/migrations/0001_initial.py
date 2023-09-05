# Generated by Django 4.2.4 on 2023-09-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('Description', models.TextField()),
                ('Tag', models.CharField(max_length=32)),
                ('Price', models.IntegerField(max_length=15)),
                ('Image', models.ImageField(upload_to='ProductImage/')),
            ],
        ),
    ]