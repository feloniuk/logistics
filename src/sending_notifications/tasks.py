import json

import requests
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver

from main_page.models import OrderModel

from sending_notifications.celery import app


#@app.task
def sending_email(dict_obj, massage):
    order = json.load(dict_obj)
    subject = 'Transports Company'
    from_email = 's-feloniuk@ukr.net'
    to = order['email']
    massage = True
    if massage:
        html_content = """<p>&nbsp;</p>
                    <h4 style="text-align: center;">Здравствуйте&nbsp;""" + order['name'] + """</h4>
                    <p style="text-align: center;">Мы получили Вашу заявку на перевозку груза.</p>
                    <p style="text-align: center;">Из <span style="color: #00ff00;">""" + \
                       order['city_from'] + """</span> В <span style="color: #ff0000;">""" + \
                       order['city_to'] + """</p><p style="text-align: center;">Спасибо что выбрали Нас.<span>""" + \
                       """</span></p><p style="text-align: center;">Перевозим как своё!</p>""" + \
                       """<p style="text-align: center;"></p>"""
    else:
        html_content = """<p>&nbsp;</p>
                            <h4 style="text-align: center;">Здравствуйте&nbsp;""" + order['name'] + """</h4>
                            <p style="text-align: center;">Мы получили Вашу заявку на обратный звонок.</p>
                            <p style="text-align: center;">В ближайшее время Мы свяжемся с Вами"></p>
                            <p style="text-align: center;">Спасибо что выбрали Нас.""" + \
                       """></p><p style="text-align: center;">Перевозим как своё!</p>""" + \
                       """<p style="text-align: center;"></p>"""
    msg = EmailMessage(subject, html_content, from_email, [to])
    msg.content_subtype = "html"
    msg.send()


#@app.task
def send_order_telegram(sender, instance, created, **kwargs):
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


# @receiver(post_save, sender=CallBack)
def send_order_telegram(sender, instance, created, **kwargs):
    if created:
        token = "1541442470:AAGqE3YqpvWylc3U5_0_AOrtGjlO-SRnbgA"
        url = "https://api.telegram.org/bot"
        channel_id = "@transportage_dima"
        url += token
        method = url + "/sendMessage"
        text = "Заказ перезона от " + instance.name + ": " + str(instance.phone)

        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })

        if r.status_code != 200:
            raise Exception("post_text error")