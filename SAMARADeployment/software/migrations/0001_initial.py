# Generated by Django 4.0.5 on 2022-06-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('pagetype', models.CharField(max_length=10)),
                ('teamname', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=4)),
                ('pagetext', models.TextField()),
            ],
        ),
    ]
