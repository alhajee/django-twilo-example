import datetime

from django.db import models
from django.utils import timezone

class Inbox(models.Model):
    message_text = models.CharField(max_length=640)
    sender = models.CharField(max_length=50)
    receive_date = models.DateTimeField('date received')

    def __str__(self):
        return self.message_text + ", " + \
               self.sender + ", " + \
               self.receive_date.strftime('%Y-%m-%d %H:%M')

    def was_received_recently(self):
        return self.receive_date >= timezone.now() - datetime.timedelta(days=1)

