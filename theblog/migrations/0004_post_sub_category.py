# Generated by Django 4.1.2 on 2022-10-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_post_snippet_image_post_isfeatured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sub_category',
            field=models.ManyToManyField(blank=True, null=True, to='theblog.subcategory'),
        ),
    ]
