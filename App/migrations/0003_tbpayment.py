# Generated by Django 4.2.4 on 2023-08-31 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_rout_bus_route_rename_rout_train_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='TBpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]