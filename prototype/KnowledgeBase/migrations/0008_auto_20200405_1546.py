# Generated by Django 3.0.4 on 2020-04-05 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0007_auto_20200405_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='rank',
            new_name='answerRank',
        ),
        migrations.AddField(
            model_name='answer',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
