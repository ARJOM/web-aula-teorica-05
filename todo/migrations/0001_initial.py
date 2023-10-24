# Generated by Django 3.2.22 on 2023-10-24 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feito', models.BooleanField(default=False)),
                ('descricao', models.CharField(max_length=150)),
                ('prazo', models.DateField()),
            ],
        ),
    ]
