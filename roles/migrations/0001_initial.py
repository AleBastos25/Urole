# Generated by Django 4.2.5 on 2023-11-21 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dia', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('poster_url', models.URLField(null=True)),
            ],
        ),
    ]