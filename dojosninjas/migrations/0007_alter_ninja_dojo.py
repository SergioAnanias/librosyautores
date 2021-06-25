# Generated by Django 3.2.4 on 2021-06-13 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojosninjas', '0006_remove_dojo_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(default='null', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ninjas', to='dojosninjas.dojo'),
        ),
    ]
