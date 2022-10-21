# Generated by Django 4.1.2 on 2022-10-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_post_isfeatured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet_image',
            field=models.ImageField(blank=True, null=True, upload_to='snippet-image/'),
        ),
        migrations.AddConstraint(
            model_name='post',
            constraint=models.UniqueConstraint(condition=models.Q(('isFeatured', True)), fields=('isFeatured',), name='isFeatured'),
        ),
    ]