# Generated by Django 3.1.5 on 2021-02-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_auto_20210216_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='phone',
            field=models.PositiveIntegerField(help_text='Телефон', verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='сargo_from',
            field=models.PositiveSmallIntegerField(help_text='Масса от, кг', verbose_name='Масса от, кг'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='сargo_to',
            field=models.PositiveSmallIntegerField(help_text='Масса до, кг', verbose_name='Масса до, кг'),
        ),
        migrations.AlterField(
            model_name='statistics_info',
            name='clients',
            field=models.PositiveIntegerField(max_length=255, verbose_name='Довольных клиентов'),
        ),
        migrations.AlterField(
            model_name='statistics_info',
            name='reviews',
            field=models.PositiveSmallIntegerField(max_length=255, verbose_name='Отзывы'),
        ),
        migrations.AlterField(
            model_name='statistics_info',
            name='vehicle',
            field=models.PositiveSmallIntegerField(max_length=255, verbose_name='Транспортных средств'),
        ),
        migrations.AlterField(
            model_name='statistics_info',
            name='years',
            field=models.PositiveSmallIntegerField(max_length=255, verbose_name='Лет службы'),
        ),
    ]
