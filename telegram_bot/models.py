from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=100)
    chat_id = models.BigIntegerField()

    def __str__(self):
        return self.username

