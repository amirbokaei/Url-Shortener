# Generated by Django 3.2.6 on 2021-10-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='url_shorten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgin_url', models.CharField(max_length=300)),
                ('short_url', models.CharField(max_length=100)),
            ],
        ),
    ]
