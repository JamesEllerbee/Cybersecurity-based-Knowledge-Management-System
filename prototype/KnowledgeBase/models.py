from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Asset(models.Model):
    assetName = models.CharField(max_length=30)


class Threat(models.Model):
    threatName = models.CharField(max_length=100)
    assetKey = models.ForeignKey(Asset, on_delete=models.CASCADE)


class Advice(models.Model):
    adviceText = models.CharField(max_length=200)
    threatKey = models.ForeignKey(Threat, on_delete=models.CASCADE)


class Question(models.Model):
    questionText = models.CharField(max_length=200)
    assetKey = models.ForeignKey(Asset, on_delete=models.CASCADE)


class Answer(models.Model):
    answerText = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
