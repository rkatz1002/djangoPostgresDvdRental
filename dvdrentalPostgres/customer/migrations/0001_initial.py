# Generated by Django 3.0.5 on 2020-04-19 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_id', models.SmallIntegerField()),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('activebool', models.BooleanField()),
                ('create_date', models.DateField()),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('active', models.IntegerField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='staff.Address')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
