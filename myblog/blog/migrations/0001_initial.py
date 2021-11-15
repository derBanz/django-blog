# Generated by Django 3.2.8 on 2021-11-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=16)),
            ],
        ),
    ]
