# Generated by Django 3.2.8 on 2021-11-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0014_auto_20211101_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Backend', 'Backend'), ('Frontend', 'Frontend'), ('Fullstack', 'Fullstack')], max_length=20),
        ),
    ]