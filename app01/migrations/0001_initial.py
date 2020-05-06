# Generated by Django 3.0.2 on 2020-04-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='书名')),
                ('pv', models.IntegerField(default=0, verbose_name='浏览量')),
            ],
            options={
                'verbose_name': '图书表',
                'verbose_name_plural': '图书表',
            },
        ),
    ]
