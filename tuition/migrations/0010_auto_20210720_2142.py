# Generated by Django 3.1.5 on 2021-07-20 15:42

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0009_auto_20210617_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='medium',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Korea', 'Korea'), ('Bangla', 'Bangla'), ('English', 'English'), ('Japanis', 'Japanis'), ('China', 'China')], default='Bangla', max_length=100),
        ),
    ]
