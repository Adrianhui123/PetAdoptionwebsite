# Generated by Django 4.2 on 2023-11-21 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('available', 'Available'), ('adopted', 'Adopted'), ('canceled', 'Canceled')], default='available', max_length=10)),
                ('species', models.CharField(max_length=255)),
                ('breed', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('m', 'M'), ('f', 'F')], default=('m', 'M'), max_length=10)),
                ('size', models.CharField(max_length=255)),
                ('medical_history', models.TextField()),
                ('behavior', models.TextField()),
                ('special_needs', models.TextField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_listings', to='accounts.shelteruser')),
            ],
        ),
    ]
