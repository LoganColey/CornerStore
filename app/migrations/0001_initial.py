# Generated by Django 3.2.7 on 2022-05-06 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='unpaid', max_length=1000, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='closingTill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='dailyLunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entree1', models.CharField(max_length=100, null=True)),
                ('entree2', models.CharField(max_length=100, null=True)),
                ('side1', models.CharField(max_length=100, null=True)),
                ('side2', models.CharField(max_length=100, null=True)),
                ('side3', models.CharField(max_length=100, null=True)),
                ('bread', models.CharField(max_length=100, null=True)),
                ('dessert', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='menuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.CharField(max_length=400)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='noOrdersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='cartItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('name', models.CharField(default='no name', max_length=100)),
                ('type', models.CharField(default='no type', max_length=20)),
                ('side1', models.CharField(choices=[('--Choose a Side--', (('corn nuggets', 'Corn Nuggets'), ('tater tots', 'Tater Tots'), ('french fries', 'French Fries'), ('onion rings', 'Onion Rings'), ('fried okra', 'Fried Okra'), ('loaded baked potato', 'Loaded Baked Potato + $2.50'), ('side salad', 'Side Salad + $2.50')))], max_length=20)),
                ('side2', models.CharField(choices=[('--Choose a Side--', (('corn nuggets', 'Corn Nuggets'), ('tater tots', 'Tater Tots'), ('french fries', 'French Fries'), ('onion rings', 'Onion Rings'), ('fried okra', 'Fried Okra'), ('loaded baked potato', 'Loaded Baked Potato + $2.50'), ('side salad', 'Side Salad + $2.50')))], max_length=20)),
                ('comment', models.CharField(blank=True, max_length=1000)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cart')),
            ],
        ),
    ]
