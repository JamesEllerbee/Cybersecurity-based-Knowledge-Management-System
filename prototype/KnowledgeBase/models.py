from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.


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
    vulnerabilityKey = models.ForeignKey('Vulnerability', on_delete=models.PROTECT, null=True)
    assetKey = models.ForeignKey('Asset', on_delete=models.CASCADE)
    adviceKey = models.ForeignKey('Advice', on_delete=models.PROTECT, null=True)
    threatName = models.CharField(max_length=100)

    class meta:
        managed = False
        db_table = 'threat'

    def __str__(self):
        return self.threatName



'''
TABLE NAME: 
    Question
        holds What questions have been posted in the system
COLUMNS
    assetKey
        is the forgin key to the assetKey this quesitons is tied too
    date
        the date this question was created
    questionRank
        the rank of the question
    questionText
        is the question itself
'''
class Question(models.Model):
    assetKey = models.ForeignKey('Asset', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, auto_now=False)
    questionRank = models.IntegerField(default=0)
    questionText = models.CharField(max_length=200)

    class meta:
        managed = False
        db_table = 'question'

    def __str__(self):
        return self.questionText


'''
TABLE NAME: 
    Answer
        holds What Answers have been posted in the system
COLUMNS
    question
        is the forgin key to the question this answer is tied too
    date
        the date this answer was created
    answerRank
        the rank of the answer
    answerText
        is the answer itself
'''
class Answer(models.Model):
     #TODO: change this to question key and any parts in the code base to match, will also have to change name in admin.py too
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, auto_now=False)
    answerRank = models.IntegerField(primary_key=False, default=0)
    answerText = models.CharField(max_length=200)
  
    class meta:
        managed = False
        db_table = 'answer'

    def __str__(self):
        return self.answerText


'''
TABLE NAME: 
    Vulnerability
        holds information about vulnerabilitys on the system
COLUMNS
    assetKey
        is the forgin key to the asset this vulnerability is tied too
    threatKey
        is the forgin key to the threat this vulnerability is tied too
    attackerKey
        is the forgin key to the attacker this vulnerability is tied too
    countermeasureKey
        is the forgin key to the counter measure this vulnerability is tied too
    ciaaKey
        is the forgin key to the CIAA this vulnerability is tied too
    severityLevelKey
        is the forgin key to the severity level this vulnerability is tied too
    vulterabilityText
        text explaining what the vulterability is
'''
class Vulnerability(models.Model):
    assetKey =  models.ForeignKey('Asset', on_delete=models.CASCADE)
    threatKey = models.ForeignKey('Threat', on_delete=models.CASCADE)
    attackerKey = models.ForeignKey('Attacker', on_delete=models.PROTECT, null=True)
    countermeasureKey =models.ForeignKey('Countermeasure', on_delete=models.PROTECT, null=True)
    ciaaKey = models.ForeignKey('CiaaCategory', on_delete=models.PROTECT, null=True)
    severityLevelKey = models.ForeignKey('SeverityLevel', on_delete=models.PROTECT, null=True)
    vulterabilityText = models.CharField(max_length=200)

    class meta:
        managed = False
        db_table = 'vulnerability'

    def __str__(self):
        return self.vulterabilityText


'''
TABLE NAME: 
    Severity Level
        holds the different types of severity levels on the system
COLUMNS
    vulnerabilityKey
        is the forgin key to the vulnerability this severity level is tied too
    level
        shows what level this severity is
'''
class SeverityLevel(models.Model):
    vulnerabilityKey = models.ForeignKey('Vulnerability', on_delete=models.CASCADE)
    level = models.CharField(max_length=200)

    class meta:
        managed = False
        db_table = 'severitylevel'

    def __str__(self):
        return self.level


'''
TABLE NAME: 
    Counter Measure
        holds what countermeasure are on the system 
COLUMNS
    vulnerabilityKey
        is the forgin key to the vulnerability this counter measure is tied too
    employedDate
        is the data this counter measure was created
    CountermeasureText
        is the text explaning the counter measure itself
'''
class Countermeasure(models.Model):
    vulnerabilityKey = models.ForeignKey('Vulnerability', on_delete=models.CASCADE)
    employedDate = models.DateField(auto_now_add=True, auto_now=False)
    CountermeasureText = models.CharField(max_length=200)

    class meta:
        managed = False
        db_table = 'countermeasure'

    def __str__(self):
        return self.CountermeasureText


'''
TABLE NAME: 
    Attacker
        holds the different types of attackers that are on the system
COLUMNS
    vulnerabilityKey
         is the forgin key to the vulnerability this Attacker is tied too
    attackerType
        text stating what type of attacker this attacker is
'''
class Attacker(models.Model):
    vulnerabilityKey = models.ForeignKey('Vulnerability', on_delete=models.CASCADE)
    attackerType = models.CharField(max_length=200)

    class meta:
        managed = False
        db_table = 'attacker'

    def __str__(self):
        return self.attackerType


'''
TABLE NAME: 
    Ciaa Category
        The different types of CIAA categorys are on the system
COLUMNS
    vulnerabilityKey
        is the forgin key to the vulnerability this Ciaa Category is tied too
    categoryType
        text stating what category this CIAA falls into
'''
class CiaaCategory(models.Model):
    vulnerabilityKey = models.ForeignKey('Vulnerability', on_delete=models.CASCADE)
    categoryType = models.CharField(max_length=200)

    class meta:
        managed = False
        db_table = 'ciaacategory'

    def __str__(self):
        return self.categoryType