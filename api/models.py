from django.db import models

# Create your models here.

# Models to save the reports send by the user over a message that was sent by the chatbot
class Report(models.Model):
    message_send = models.TextField()
    message_receive = models.TextField()
    date = models.DateTimeField()
    dataset_version = models.CharField(max_length=20)
    message_report = models.TextField()
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - {self.message_send[:30]}"

# Models to save the logs of every chatbot interactions

class Log(models.Model):
    pass