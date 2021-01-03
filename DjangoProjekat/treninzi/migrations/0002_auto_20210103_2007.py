# Generated by Django 3.1.4 on 2021-01-03 19:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treninzi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='content',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='practice',
            name='hours',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='practice',
            name='minutes',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AlterField(
            model_name='practice',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='practice',
            name='rate',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
