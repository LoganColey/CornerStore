# Generated by Django 3.2.7 on 2022-04-27 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20220427_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidemodel',
            name='cartItem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.menuitem'),
        ),
    ]