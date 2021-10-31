# Generated by Django 3.2.8 on 2021-10-31 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0008_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Backend', 'Backend'), ('Fullstack', 'Fullstack'), ('Frontend', 'Frontend')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], max_length=20),
        ),
    ]