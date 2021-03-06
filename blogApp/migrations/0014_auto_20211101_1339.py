# Generated by Django 3.2.8 on 2021-11-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0013_auto_20211101_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Fullstack', 'Fullstack'), ('Backend', 'Backend')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft')], max_length=20),
        ),
    ]
