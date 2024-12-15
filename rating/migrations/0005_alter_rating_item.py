# Generated by Django 3.2.4 on 2023-07-09 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
        ('rating', '0004_alter_rating_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='item.item'),
        ),
    ]
