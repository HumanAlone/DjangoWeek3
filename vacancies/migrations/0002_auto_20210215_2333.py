# Generated by Django 3.1.6 on 2021-02-15 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='company',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='specialty',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Specialty',
        ),
        migrations.DeleteModel(
            name='Vacancy',
        ),
    ]