# Generated by Django 3.1.5 on 2021-06-16 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tuition', '0007_auto_20210616_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='medium',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Korea', 'Korea'), ('English', 'English'), ('China', 'China'), ('Bangla', 'Bangla'), ('Japanis', 'Japanis')], default='Bangla', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]