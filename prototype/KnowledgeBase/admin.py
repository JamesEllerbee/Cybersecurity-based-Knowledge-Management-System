from django.contrib import admin

# Register your models here.
from .models import Asset, Question, Advice, Threat, Answer

admin.site.register(Asset)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Threat)
admin.site.register(Advice)
