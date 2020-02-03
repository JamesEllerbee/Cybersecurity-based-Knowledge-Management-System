from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Asset(models.Model):
    assetName = models.CharField(max_length=30)


class Department(models.Model):
    departmentName = models.CharField(max_length=50)
    departmentAssets = models.ManyToManyField(Asset)


class Threat(models.Model):
    threatName = models.CharField(max_length=100)
    assetKey = models.ForeignKey(Asset, on_delete=models.CASCADE)
    departmentKey = models.ForeignKey(Department, on_delete=models.PROTECT)


class Advice(models.Model):
    adviceText = models.CharField(max_length=200)
    threatKey = models.ForeignKey(Threat, on_delete=models.CASCADE)


class Question(models.Model):
    questionText = models.CharField(max_length=200)
    assetKey = models.ForeignKey(Asset, on_delete=models.CASCADE)
    departmentKey = models.ManyToManyField(Department)


class Answers(models.Model):
    answerText = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departmentKey = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    canAnswer = models.BooleanField

