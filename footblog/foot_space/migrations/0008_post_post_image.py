# Generated by Django 4.1.2 on 2022-12-12 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foot_space', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
