from django.db import models


class Inbox(models.Model):
    message_text = models.CharField(max_length=640)
    sender = models.CharField(max_length=50)
    receive_date = models.DateTimeField('date received')

