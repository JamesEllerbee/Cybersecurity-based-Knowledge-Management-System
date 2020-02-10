from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Asset(models.Model):
    assetName = models.CharField(max_length=30)

    class meta:
        managed = False
        db_table = 'asset'

    def __str__(self):
        return self.assetName


class Threat(models.Model):
    threatName = models.CharField(max_length=100)
    assetKey = models.ForeignKey(Asset, on_delete=models.CASCADE)

    class meta:
        managed = False
        db_table = 'threat'

    def __str__(self):
        return self.threatName


class Advice(models.Model):
    adviceText = models.CharField(max_length=200)
    threatKey = models.ForeignKey(Threat, on_delete=models.CASCADE)

    class meta:
        managed = False
        db_table = 'advice'

    def __str__(self):
        return self.adviceText


class Question(models.Model):
    questionText = models.CharField(max_length=200)
    assetKey = models.ForeignKey(Asset, on_delete=models.CASCADE)

    class meta:
        managed = False
        db_table = 'question'

    def __str__(self):
        return self.questionText


class Answer(models.Model):
    answerText = models.CharField(max_length=200)
    answerRank = models.IntegerField(primary_key=False, default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class meta:
        managed = False
        db_table = 'answer'

    def __str__(self):
        return self.answerText
