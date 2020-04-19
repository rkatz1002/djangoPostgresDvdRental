# Generated by Django 3.0.5 on 2020-04-19 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
        ('customer', '0001_initial'),
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('rental_id', models.AutoField(primary_key=True, serialize=False)),
                ('rental_date', models.DateTimeField()),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.Customer')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='film.Inventory')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='staff.Staff')),
            ],
            options={
                'db_table': 'rental',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('payment_date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.Customer')),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payment.Rental')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='staff.Staff')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]