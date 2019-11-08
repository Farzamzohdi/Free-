# Generated by Django 2.2.7 on 2019-11-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191108_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='first_day',
            field=models.IntegerField(choices=[('0', 'شنبه'), ('1', 'یک\u200cشنبه'), ('2', 'دوشنبه'), ('3', 'سه\u200cشنبه'), ('4', 'چهارشنبه')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='second_day',
            field=models.IntegerField(blank=True, choices=[('0', 'شنبه'), ('1', 'یک\u200cشنبه'), ('2', 'دوشنبه'), ('3', 'سه\u200cشنبه'), ('4', 'چهارشنبه')], null=True),
        ),
    ]
