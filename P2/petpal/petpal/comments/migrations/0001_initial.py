# Generated by Django 4.2 on 2023-11-21 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('creationTime', models.DateTimeField(auto_now_add=True)),
                ('username', models.TextField()),
            ],
        ),
    ]
