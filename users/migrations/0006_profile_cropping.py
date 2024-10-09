# Generated by Django 2.2.2 on 2019-06-11 10:05

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('picture', '300x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
