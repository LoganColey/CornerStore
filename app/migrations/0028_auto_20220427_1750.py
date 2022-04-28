# Generated by Django 3.2.7 on 2022-04-27 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0027_auto_20220427_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='side1',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='side2',
        ),
        migrations.CreateModel(
            name='sideModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(choices=[('--Choose a Side--', (('corn nuggets', 'Corn Nuggets'), ('tater tots', 'Tater Tots'), ('french fries', 'French Fries'), ('onion rings', 'Onion Rings'), ('fried okra', 'Fried Okra'), ('loaded baked potato', 'Loaded Baked Potato'), ('side salad', 'Side Salad')))], max_length=200, null=True)),
                ('cartItem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cartitem')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]