# Generated by Django 3.0.5 on 2020-04-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='threat',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
    ]