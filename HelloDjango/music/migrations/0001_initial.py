# Generated by Django 2.0.5 on 2018-05-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='write artist name here', max_length=100, verbose_name='Artist name')),
                ('age', models.CharField(default=18, max_length=1000, verbose_name='Age')),
            ],
        ),
    ]
