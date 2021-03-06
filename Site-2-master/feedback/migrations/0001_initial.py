# Generated by Django 4.0.3 on 2022-04-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=120, verbose_name='Email')),
                ('theme', models.CharField(max_length=100, verbose_name='Тема')),
                ('message', models.TextField(max_length=1500, verbose_name='Сообщение')),
            ],
        ),
    ]
