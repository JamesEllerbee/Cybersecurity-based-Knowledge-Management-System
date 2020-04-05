from django.contrib import admin

# Register your models here.
from .models import Asset, Question, Advice, Threat, Answer


class assetAdmin(admin.ModelAdmin):
    list_display = ("assetName",)


class adviceAdmin(admin.ModelAdmin):
    list_display = ("adviceText", "threatKey")


class questionAdmin(admin.ModelAdmin):
    list_display = ("assetKey", "date", "questionRank", "questionText",)


class threatAdmin(admin.ModelAdmin):
    #add in vulnerabilityKey
    list_display = ("assetKey", "threatName", "adviceKey")


class answerAdmin(admin.ModelAdmin):
    list_display = ("question", "date", "answerText", "answerRank")



admin.site.register(Asset, assetAdmin)
admin.site.register(Question, questionAdmin)
admin.site.register(Answer, answerAdmin)
admin.site.register(Threat, threatAdmin)
admin.site.register(Advice, adviceAdmin)
