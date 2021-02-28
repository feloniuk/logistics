from django.db import models
from django.db.models import signals
from django.forms import model_to_dict

from sending_notifications.tasks import sending_email


class CallBack(models.Model):
    name = models.CharField(max_length=50, help_text="Имя* ", blank=False, null=False)
    phone = models.DecimalField(max_digits=12, decimal_places=0, help_text="Телефон* ", blank=False, null=False)
    description = models.TextField(max_length=255, help_text="Описание", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


def send_callback_mail(sender, instance, created, **kwargs):
    if created:
        dict_obj = model_to_dict(instance)
        massage = False                      #если Тру - заказ, иначе обратный вызов
        # sending_email.delay(dict_obj, massage)


signals.post_save.connect(send_callback_mail, sender=CallBack)
