# Generated by Django 2.2.3 on 2019-08-02 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20190802_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(blank=True, default=2, max_length=100),
            preserve_default=False,
        ),
    ]
