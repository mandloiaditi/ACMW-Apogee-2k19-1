# Generated by Django 2.1.5 on 2019-02-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_playeruser_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionno', models.IntegerField()),
                ('solution', models.CharField(max_length=50)),
                ('question', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]
