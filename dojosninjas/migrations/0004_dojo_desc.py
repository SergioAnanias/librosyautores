# Generated by Django 3.2.4 on 2021-06-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojosninjas', '0003_alter_ninja_dojo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='Dojo Antiguo'),
            preserve_default=False,
        ),
    ]
