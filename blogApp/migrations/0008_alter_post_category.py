# Generated by Django 3.2.8 on 2021-10-31 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0007_auto_20211029_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Backend', 'Backend'), ('Frontend', 'Frontend'), ('Fullstack', 'Fullstack')], max_length=20),
        ),
    ]