# Generated by Django 3.1.5 on 2021-02-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя* ', max_length=50)),
                ('phone', models.DecimalField(decimal_places=0, help_text='Телефон* ', max_digits=12)),
                ('description', models.TextField(blank=True, help_text='Описание', max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
