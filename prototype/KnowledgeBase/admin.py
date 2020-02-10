from django.contrib import admin

# Register your models here.
from .models import Asset, Question, Advice, Threat, Answer


class assetAdmin(admin.ModelAdmin):
    list_display = ("assetName",)


class questionAdmin(admin.ModelAdmin):
    list_display = ("assetKey", "questionText",)


class threatAdmin(admin.ModelAdmin):
    list_display = ("assetKey", "threatName",)


class answerAdmin(admin.ModelAdmin):
    list_display = ("question", "answerText",)


class adviceAdmin(admin.ModelAdmin):
    list_display = ("threatKey", "adviceText",)


admin.site.register(Asset, assetAdmin)
admin.site.register(Question, questionAdmin)
admin.site.register(Answer, answerAdmin)
admin.site.register(Threat, threatAdmin)
admin.site.register(Advice, adviceAdmin)
