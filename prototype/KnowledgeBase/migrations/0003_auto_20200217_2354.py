# Generated by Django 3.0.3 on 2020-02-17 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0002_answer_answerrank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advice',
            name='threatKey',
        ),
        migrations.AddField(
            model_name='threat',
            name='adviceKey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='KnowledgeBase.Advice'),
        ),
    ]
