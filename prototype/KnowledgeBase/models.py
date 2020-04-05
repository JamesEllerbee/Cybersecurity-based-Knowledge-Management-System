from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.


'''
TABLE NAME: 
    somthing
        somthing
COLUMNS
    something
        for this
    something
        for this
'''

'''
TABLE NAME: 
    Asset
        holds what assets are in the system
COLUMNS
    assetName
        holds the name of the Asset
'''
class Asset(models.Model):
    assetName = models.CharField(max_length=30)

    class meta:
        managed = False
        db_table = 'asset'

    def __str__(self):
        return self.assetName


'''
TABLE NAME: 
    Advice
        holds advice that can be tied to threats in the system
COLUMNS
    threatID
        holds the ID of the threat record this advice is tied too
    adviceText
        holds text that is the advice itself
'''
class Advice(models.Model):
    #FIXME: this might need to be thread id? check dev branch
    threatKey = models.ForeignKey('Threat', on_delete=models.PROTECT, null=True)
    adviceText = models.CharField(max_length=200)

    class meta:
        managed = False
        db_table = 'advice'

    def __str__(self):
        return self.adviceText


'''
TABLE NAME: 
    Threat
        Holds threats that are used in the system
COLUMNS
    vulnerabilityKey
        is the forgin key to the vulernability table
    assetKey
        is the forgin key to a record in the asset table
    adviceKey
        is the forgin key to a record in the advice table
    threatName
        is the name of this threat
'''
class Threat(models.Model):
    #vulnerabilityKey = ('Vulnerability', on_delete=models.PROTECT, null=True)
    assetKey = models.ForeignKey('Asset', on_delete=models.CASCADE)
    adviceKey = models.ForeignKey('Advice', on_delete=models.PROTECT, null=True)
    threatName = models.CharField(max_length=100)

    class meta:
        managed = False
        db_table = 'threat'

    def __str__(self):
        return self.threatName


class Question(models.Model):
    assetKey = models.ForeignKey('Asset', on_delete=models.CASCADE)
    #FIXME:figure this out
    date = models.DateField(auto_now_add=True)
    rank = models.IntegerField(default=0)
    questionText = models.CharField(max_length=200)

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
