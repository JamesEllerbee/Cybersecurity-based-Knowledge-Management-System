from django.contrib import admin

# Register your models here.
from .models import Asset, Question, Advice, Threat, Answer, Vulnerability, SeverityLevel, \
                    Countermeasure, Attacker, CiaaCategory

                    


class assetAdmin(admin.ModelAdmin):
    list_display = ("assetName",)


class adviceAdmin(admin.ModelAdmin):
    list_display = ("adviceText", "threatKey")


class questionAdmin(admin.ModelAdmin):
    list_display = ("assetKey", "date", "questionRank", "questionText",)


class threatAdmin(admin.ModelAdmin):
    list_display = ("assetKey", "vulnerabilityKey", "threatName", "adviceKey")


class answerAdmin(admin.ModelAdmin):
    list_display = ("question", "date", "answerText", "answerRank")


class vulnerabilityAdmin(admin.ModelAdmin):
    #TODO:add in the other fields
    list_display = ("assetKey", "threatKey", "attackerKey", "countermeasureKey", "ciaaKey", "severityLevelKey", "vulterabilityText")


class severitylevelAdmin(admin.ModelAdmin):
    list_display = ("vulnerabilityKey", "level")


class countermeasureAdmin(admin.ModelAdmin):
    list_display = ("vulnerabilityKey", "employedDate", "CountermeasureText")


class attackerAdmin(admin.ModelAdmin):
    list_display = ("vulnerabilityKey", "attackerType")


class ciaacategoryAdmin(admin.ModelAdmin):
    list_display = ("vulnerabilityKey", "categoryType")



admin.site.register(Asset, assetAdmin)
admin.site.register(Question, questionAdmin)
admin.site.register(Answer, answerAdmin)
admin.site.register(Threat, threatAdmin)
admin.site.register(Advice, adviceAdmin)
admin.site.register(Vulnerability, vulnerabilityAdmin)
admin.site.register(SeverityLevel, severitylevelAdmin)
admin.site.register(Countermeasure, countermeasureAdmin)
admin.site.register(Attacker, attackerAdmin)
admin.site.register(CiaaCategory, ciaacategoryAdmin)
