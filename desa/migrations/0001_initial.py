# Generated by Django 2.2.12 on 2020-04-27 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desa',
            fields=[
                ('idDesa', models.AutoField(primary_key=True, serialize=False)),
                ('namaDesa', models.CharField(max_length=100)),
                ('totalAnak', models.IntegerField(default=0)),
            ],
        ),
    ]
