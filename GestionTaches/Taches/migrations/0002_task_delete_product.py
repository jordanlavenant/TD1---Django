# Generated by Django 5.1.1 on 2024-09-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
