# Generated by Django 4.2.4 on 2023-08-28 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('row', '0004_movieshots'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='row.reviews', verbose_name='Родитель'),
        ),
    ]