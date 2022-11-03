# Generated by Django 4.1.2 on 2022-10-31 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_remove_product_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WinningProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.CharField(max_length=255)),
                ('product_url_1', models.TextField(default='default')),
                ('product_url_2', models.TextField(default='default')),
                ('product_url_3', models.TextField(default='default')),
                ('product_seller_1', models.CharField(default='default', max_length=255)),
                ('product_seller_2', models.CharField(default='default', max_length=255)),
                ('product_seller_3', models.CharField(default='default', max_length=255)),
                ('product_price_1', models.CharField(default='£', max_length=255)),
                ('product_price_2', models.CharField(default='£', max_length=255)),
                ('product_price_3', models.CharField(default='£', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='chosen_product',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_1',
            field=models.CharField(default='£', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_2',
            field=models.CharField(default='£', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_3',
            field=models.CharField(default='£', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='winning_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='theblog.winningproduct'),
        ),
    ]