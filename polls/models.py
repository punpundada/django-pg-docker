from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):

    def __str__(self):
        return str({"question_text": self.question_text,"pub_date":self.pub_date})
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name="date published")


class Choice(models.Model):

    def __str__(self):
        return str({"choice_text":self.choice_text,"votes":self.votes})

    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
