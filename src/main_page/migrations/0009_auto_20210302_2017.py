# Generated by Django 3.1.5 on 2021-03-02 18:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_auto_20210302_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='date',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='date1',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='date2',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='nomination',
            field=models.CharField(default=django.utils.timezone.now, help_text='Наименование', max_length=100, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='tipe_loads',
            field=models.CharField(blank=True, choices=[('Верхняя', 'Верхняя'), ('Боковая', 'Боковая'), ('Задняя', 'Задняя'), ('С полной растеновкой', 'С полной растеновкой'), ('Со снятием поперечин', 'Со снятием поперечин'), ('Со снятием стоек', 'Со снятием стоек'), ('Без ворот', 'Без ворот')], help_text='Тип погрузки', max_length=255, null=True, verbose_name='Тип погрузки'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(help_text='ФИО отправителя', max_length=100, verbose_name='ФИО отправителя'),
        ),
    ]