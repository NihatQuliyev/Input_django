# Generated by Django 4.1.3 on 2022-11-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=20)),
                ('name', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
