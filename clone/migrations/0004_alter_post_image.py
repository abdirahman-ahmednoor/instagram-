# Generated by Django 3.2.7 on 2021-09-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts'),
        ),
    ]
