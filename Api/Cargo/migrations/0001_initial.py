# Generated by Django 4.0.2 on 2022-04-26 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.base')),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('slogan', models.CharField(db_column='Slogan', max_length=255, unique=True)),
                ('phone_number', models.CharField(db_column='Phone_Number', max_length=255)),
                ('is_active', models.BooleanField(db_column='IsActive', default=True, help_text='I will use this for enable/disable a specific record')),
            ],
            bases=('main.base',),
        ),
    ]
