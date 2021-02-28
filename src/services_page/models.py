from django.db import models


class ServiceModel(models.Model):
    title = models.CharField(max_length=50, help_text="Имя* ", blank=False, null=False)
    description = models.TextField(max_length=255, help_text="Описание", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
