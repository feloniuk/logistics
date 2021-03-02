import requests
from django.db import models
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict


class OrderModel(models.Model):
    class Meta:
        verbose_name = 'Плановый заказ'
        verbose_name_plural = 'Плановые заказы'

    FORM_PAY = (
        ('Наличные', 'Наличные'),
        ('Безнал.', 'Безнал.'),
        ('Комб.', 'Комб.'),
    )
    MOMENT_PAY = (
        ('На загрузке', 'На загрузке'),
        ('На выгрузке', 'На выгрузке'),
    )
    TIPE_LOADS = (
        ('Верхняя', 'Верхняя'),
        ('Боковая', 'Боковая'),
        ('Задняя', 'Задняя'),
        ('С полной растеновкой', 'С полной растеновкой'),
        ('Со снятием поперечин', 'Со снятием поперечин'),
        ('Со снятием стоек', 'Со снятием стоек'),
        ('Без ворот', 'Без ворот'),
    )
    CATEGORY_VEHICLES = (
        ('Крытая', (
            ('тент', 'Тент'),
            ('цельномет', 'Цельномет'),
            ('Бус', 'Бус'),
            ('Контейнер', 'Контейнер'),
            ('Одеждовоз', 'Одеждовоз'),
            ('Изотерм', 'Изотерм'),
            ('Реф', 'Реф'),
            ('Реф.-тушевоз', 'Реф.-тушевоз'),
        )
         ),
        ('Открытая', (
            ('Бортовая/Открытая', 'Бортовая/Открытая'),
            ('Платформа', 'Платформа'),
            ('Бензовоз', 'Бензовоз'),
            ('Газовоз', 'Газовоз'),
            ('Кормовоз', 'Кормовоз'),
            ('Муковоз', 'Муковоз'),
            ('Автоцистерна', 'Автоцистерна'),
            ('Цементовоз', 'Цементовоз'),
        )
         ),
        ('Цистерна', (
            ('Молоковоз', 'Молоковоз'),
            ('Битумовоз', 'Битумовоз'),
            ('Манипулятор', 'Манипулятор'),
            ('Ломовоз/Металовоз', 'Ломовоз/Металовоз'),
            ('Контейнеровоз', 'Контейнеровоз'),
            ('Трал/Негабарит', 'Трал/Негабарит'),
            ('Плитовоз', 'Плитовоз'),
            ('Самосвал', 'Самосвал'),
        )
         ),
        ('Спец. транспорт', (
            ('Автовоз', 'Автовоз'),
            ('Бетоновоз', 'Бетоновоз'),
            ('Зерновоз', 'Зерновоз'),
            ('Лесовоз', 'Лесовоз'),
            ('Коневоз', 'Коневоз'),
            ('Кран', 'Кран'),
            ('Мусоровоз', 'Мусоровоз'),
            ('Погрузчик', 'Погрузчик'),
            ('Птицевоз', 'Птицевоз'),
            ('Скотовоз', 'Скотовоз'),
            ('Стекловоз', 'Стекловоз'),
            ('Трубовз', 'Трубовз'),
            ('Тягач', 'Тягач'),
            ('Евакуатор', 'Евакуатор'),
            ('Яхтовоз', 'Яхтовоз'),
        )
         ),
        ('Пассажирский', (
            ('микроавтобус', 'Микроавтобус'),
            ('автобус', 'Автобус'),
        )
         ),
        ('unknown', 'Unknown'),
    )

    name = models.CharField(max_length=100, verbose_name='ФИО отправителя', help_text="ФИО отправителя", blank=False,
                            null=False)
    nomination = models.CharField(max_length=100, verbose_name='Наименование', help_text="Наименование",
                                  blank=False, null=False)
    notes = models.CharField(max_length=100, verbose_name='Примечание', help_text="Примечание",
                             blank=True, null=True)
    phone = models.PositiveIntegerField(verbose_name='Телефон', help_text="Телефон", blank=False, null=False)
    email = models.EmailField(help_text="Почта", blank=False, null=False)
    receiver_name = models.CharField(max_length=50, verbose_name='ФИО получателя', help_text="ФИО получателя",
                                     blank=False, null=False)
    region_from = models.CharField(max_length=255, verbose_name='Область отправления', help_text='Область отправления',
                                   blank=False,
                                   null=False)
    region_to = models.CharField(max_length=255, verbose_name='Область прибытия', help_text='Область прибытия',
                                 blank=False, null=False)
    city_from = models.CharField(max_length=255, verbose_name='Город отправления', help_text='Город отправления',
                                 blank=False,
                                 null=False)
    city_to = models.CharField(max_length=255, verbose_name='Город прибытия', help_text='Город прибытия', blank=False,
                               null=False)
    сargo_from = models.PositiveSmallIntegerField(verbose_name='Масса от, кг', help_text='Масса от, кг', blank=False,
                                                  null=False)
    сargo_to = models.PositiveSmallIntegerField(verbose_name='Масса до, кг', help_text='Масса до, кг', blank=False,
                                                null=False)
    tipe_vehicle = models.CharField(choices=CATEGORY_VEHICLES, max_length=255, verbose_name='Тип грузовика',
                                    help_text='Тип грузовика', blank=True, null=True)
    tipe_loads = models.CharField(choices=TIPE_LOADS, max_length=255, verbose_name='Тип погрузки',
                                  help_text='Тип погрузки', blank=True, null=True)
    value_cargo_from = models.IntegerField(verbose_name='Обьем от, м3', help_text='Обьем от, м3', blank=True, null=True)
    value_cargo_to = models.IntegerField(verbose_name='Обьем до, м3', help_text='Обьем до, м3', blank=True, null=True)
    dimensions_length = models.PositiveSmallIntegerField(help_text='длина', blank=True,
                                                         null=True)
    dimensions_height = models.PositiveSmallIntegerField(help_text='высота', blank=True,
                                                         null=True)
    dimensions_width = models.PositiveSmallIntegerField(help_text='ширина', blank=True,
                                                        null=True)
    quantity_vehicles = models.PositiveSmallIntegerField(verbose_name='Кол-во авто', help_text='Кол-во авто',
                                                         blank=True, null=True)
    form_pay = models.CharField(choices=FORM_PAY, max_length=255, verbose_name='форма оплаты',
                                help_text='Форма оплаты', blank=True, null=True)
    moment_pay = models.CharField(choices=MOMENT_PAY, max_length=255, verbose_name='Момент оплаты',
                                  help_text='Момент оплаты', blank=True, null=True)
    photo = models.ImageField(upload_to='photo_order/')
    date1 = models.DateField(blank=False, null=False)
    date2 = models.DateField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.city_from} --> {self.city_to}'


class statistics_info(models.Model):
    class Meta:
        verbose_name = 'Фейк-счётчик'
        verbose_name_plural = 'Фейк-счётчики'

    vehicle = models.PositiveSmallIntegerField(verbose_name='Транспортных средств')
    reviews = models.PositiveSmallIntegerField(verbose_name='Отзывы')
    years = models.PositiveSmallIntegerField(verbose_name='Лет службы')
    clients = models.PositiveIntegerField(verbose_name='Довольных клиентов')

    def __str__(self):
        return f'Фейквые значения {self.id}'


# @receiver(post_save, sender=OrderModel)
def send_telegram(sender, instance, created, **kwargs):
    if created:
        token = "1541442470:AAGqE3YqpvWylc3U5_0_AOrtGjlO-SRnbgA"
        url = "https://api.telegram.org/bot"
        channel_id = "@transportage_dima"
        url += token
        method = url + "/sendMessage"
        text = "Внимание! Новый заказ от (" + instance.name + ") " + str(instance.phone) + " из " + instance.city_from

        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })

        if r.status_code != 200:
            raise Exception("post_text error")

