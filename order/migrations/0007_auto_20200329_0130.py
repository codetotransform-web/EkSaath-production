# Generated by Django 3.0.4 on 2020-03-28 20:00

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_unconfirmed_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unconfirmed_order',
            old_name='added_tocart_date',
            new_name='added_to_order_date',
        ),
        migrations.AddField(
            model_name='unconfirmed_order',
            name='delivery_city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unconfirmed_order',
            name='delivery_colony',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unconfirmed_order',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
    ]
