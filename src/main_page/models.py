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

    name = models.CharField(max_length=50, verbose_name='ФИО отправителя', help_text="ФИО отправителя", blank=False,
                            null=False)
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
    tipe_vehicle = models.CharField(max_length=255, verbose_name='Тип грузовика', help_text='Тип грузовика', blank=True,
                                    null=True)
    value_cargo_from = models.IntegerField(verbose_name='Обьем от, м3', help_text='Обьем от, м3', blank=True, null=True)
    value_cargo_to = models.IntegerField(verbose_name='Обьем до, м3', help_text='Обьем до, м3', blank=True, null=True)
    date = models.DateField(verbose_name='Дата', help_text='Дата', blank=True, null=True)
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

# @receiver(post_save, sender=OrderModel)
# def send_order_mail(sender, instance, created, **kwargs):
#     if created:
#         dict_obj = model_to_dict(instance)
#         massage = True                      #если Тру - заказ, иначе обратный вызов
#         sending_email.delay(dict_obj, massage)
