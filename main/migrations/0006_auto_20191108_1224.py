# Generated by Django 2.2.7 on 2019-11-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191108_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date',
            field=models.DateField(default='2020-10-10'),
        ),
        migrations.AlterField(
            model_name='course',
            name='first_day',
            field=models.IntegerField(choices=[(0, 'شنبه'), (1, 'یک\u200cشنبه'), (2, 'دوشنبه'), (3, 'سه\u200cشنبه'), (4, 'چهارشنبه')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='second_day',
            field=models.IntegerField(blank=True, choices=[(0, 'شنبه'), (1, 'یک\u200cشنبه'), (2, 'دوشنبه'), (3, 'سه\u200cشنبه'), (4, 'چهارشنبه')], null=True),
        ),
    ]
