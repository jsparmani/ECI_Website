# Generated by Django 2.1.5 on 2019-02-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_voter_phone_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='govuser',
            name='is_supergov',
            field=models.BooleanField(default=False),
        ),
    ]
